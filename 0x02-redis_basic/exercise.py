#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from functools import wraps
import redis
import uuid
from typing import Union
from typing import Callable


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.

    Args:
        method: The method to be counted.

    Returns:
        Callable: Decorated method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count and returns the
          original result.

        Args:
            self: The instance of the Cache class.
            *args: Arguments for the method.
            **kwargs: Keyword arguments for the method.

        Returns:
            Any: The result of the original method.
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self):
        """
        Initialize the Cache class. Create a Redis client and flush the Redis
          database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis and return a randomly generated key.

        Args:
            data: The data to be stored. It can be a str, bytes, int, or float.

        Returns:
            str: The randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int,
                                                          float]:
        """
        Retrieve data from Redis for the given key and optionally convert it
          using the provided callable function.

        Args:
            key: The key to retrieve data from.
            fn: A callable function to convert the data (optional).

        Returns:
            Union[str, bytes, int, float]: The retrieved data, optionally
              converted.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data) if data else data
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis as a string.

        Args:
            key: The key to retrieve data from.

        Returns:
            str: The retrieved data as a string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis as an integer.

        Args:
            key: The key to retrieve data from.

        Returns:
            int: The retrieved data as an integer.
        """
        return self.get(key, fn=lambda d: int(d))


if __name__ == "__main__":
    cache = Cache()

    # Applying the count_calls decorator to the store method
    cache.store = cache.count_calls(cache.store)

    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))

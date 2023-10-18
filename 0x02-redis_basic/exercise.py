#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union


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


if __name__ == "__main":
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))

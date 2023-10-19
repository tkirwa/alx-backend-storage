#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from functools import wraps
import redis
from uuid import uuid4
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """Decorator that counts calls made to the method."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function for decorator functionality."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a method.

    Args:
        method (Callable): The method to store the history for.

    Returns:
        Callable: The wrapped method that stores the history.
    """
    key = method.__qualname__
    inputs, outputs = key + ":inputs", key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapped function that stores input parameters and the output.

        Args:
            self: The instance of the class.
            *args: Positional arguments for the method.
            **kwargs: Keyword arguments for the method.

        Returns:
            Any: The result of the original method.
        """
        # Convert the input arguments to a string and store them in Redis list
        input_str = str(args)
        self._redis.rpush(inputs, input_str)

        # Call the original method and get its output
        result = method(self, *args, **kwargs)

        # Store the output result in Redis list
        result_str = str(result)
        self._redis.rpush(outputs, result_str)

        return result

    return wrapper


def replay(method: Callable):
    """
    Function to display the history of calls of a particular function.

    Args:
        method (Callable): The method for which to display the history
          of calls.

    Returns:
        None
    """
    # Get the qualified name of the method
    key = method.__qualname__

    # Get the count of calls to this method from Redis
    calls = method.__self__._redis.get(key)

    # Print the count of calls to this method
    print(f"{key} was called {calls.decode('utf-8')} times:")

    # Get the inputs and outputs of all calls to this method from Redis
    inputs = method.__self__._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = method.__self__._redis.lrange(f"{key}:outputs", 0, -1)

    # Print the inputs and outputs of all calls to this method
    for inp, out in zip(inputs, outputs):
        print(f"{key}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


class Cache:
    def __init__(self):
        """
        Initialize the Cache class. Create a Redis client and flush the Redis
          database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis and return a randomly generated key.

        Args:
            data: The data to be stored. It can be a str, bytes, int, or float.

        Returns:
            str: The randomly generated key used to store the data in Redis.
        """
        key = str(uuid4())
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

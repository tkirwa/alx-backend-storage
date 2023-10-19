#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from functools import wraps
import redis
from uuid import uuid4
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called.

    Args:
        method (Callable): The method to be counted.

    Returns:
        Callable: The wrapped method that counts the calls.
    """
    # Use the qualified name of the method as the key
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapped function that increments the call count and calls the
        original method.

        Args:
            self: The instance of the class.
            *args: Positional arguments for the method.
            **kwargs: Keyword arguments for the method.

        Returns:
            Any: The result of the original method.
        """
        # Increment the call count for the method using the Redis INCR command.
        self._redis.incr(key)
        # Call the original method and return its result.
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


def replay(method: Callable) -> None:
    """Display the history of calls for a particular function.

    Args:
        method (Callable): The method to display the history for.
    """
    # Generate keys for input and output lists based on the method's
    #  qualified name
    key = method.__qualname__
    inputs, outputs = key + ":inputs", key + ":outputs"

    # Get the Redis instance from the method's instance
    redis = method.__self__._redis

    # Get the count of how many times the method was called from Redis
    count = redis.get(key).decode("utf-8")
    print(f"{key} was called {count} times:")

    # Retrieve input and output lists from Redis
    input_list = redis.lrange(inputs, 0, -1)
    output_list = redis.lrange(outputs, 0, -1)

    # Iterate over the input and output pairs and print them
    IOTuple = zip(input_list, output_list)
    for inp, outp in list(IOTuple):
        attr, data = inp.decode("utf-8"), outp.decode("utf-8")
        print(f"{key}(*{attr}) -> {data}")


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

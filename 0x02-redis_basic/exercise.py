#!/usr/bin/env python3

import redis
import uuid

"""
Writing strings to Redis
"""


class Cache:
    def __init__(self):
        # Initialize the Redis client and flush the instance
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """
        Store the input data in Redis and return a randomly generated key.

        Args:
            data: The data to be stored, which can be str, bytes, int,
              or float.

        Returns:
            str: A randomly generated key used to store the data in Redis.
        """
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        # Store the data in Redis with the generated key
        self._redis.set(key, data)
        return key


if __name__ == "__main__":
    # Example usage
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))

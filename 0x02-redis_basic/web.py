#!/usr/bin/env python3
"""Web Cache and Tracker"""

import redis
import requests
from functools import wraps
from typing import Callable

# Initialize a Redis client
redis_client = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator to count and cache requests"""

    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function for counting and caching requests"""
        # Increment the count for the URL
        redis_client.incr(f"count:{url}")

        # Check if the response is cached
        cached_response = redis_client.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode("utf-8")

        # If not cached, make a request
        response = method(url)

        # Cache the response with a 10-second expiration time
        redis_client.setex(f"cached:{url}", 10, response)

        return response

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Fetch the HTML content of a URL"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    # Example usage of the get_page function
    url = "http://slowwly.robertomurray.co.uk"
    content = get_page(url)
    print(f"Content of {url} (cached):")
    print(content)

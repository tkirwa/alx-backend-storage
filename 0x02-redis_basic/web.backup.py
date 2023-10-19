#!/usr/bin/env python3
""" web.py """

import requests
import redis
from typing import Callable
from functools import wraps

# Create a connection to the Redis server
r = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """Decorator that counts calls made to the method."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(url):
        """Wrapper function for decorator functionality."""
        r.incr(key)
        return method(url)

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """Get the HTML content of a particular URL and cache it."""
    resp = requests.get(url)
    page = resp.text

    # Cache the result with an expiration time of 10 seconds
    r.setex(url, 10, page)

    return page


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")

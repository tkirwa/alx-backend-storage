#!/usr/bin/env python3
""" web.py """

import requests
import redis
from typing import Callable
from functools import wraps

# Create a connection to the Redis server
r = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts calls made to the method.

    Args:
        method (Callable): The method for which to count calls.

    Returns:
        Callable: The decorated method.
    """
    # Get the qualified name of the method
    key = method.__qualname__

    @wraps(method)
    def wrapper(url):
        """
        Wrapper function for decorator functionality.

        Args:
            url (str): The URL to get the page from.

        Returns:
            str: The HTML content of the page.
        """
        # Increment the count for this method in Redis
        r.incr(key)
        return method(url)

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL and cache it.

    Args:
        url (str): The URL to get the page from.

    Returns:
        str: The HTML content of the page.
    """
    # Send a GET request to the URL
    resp = requests.get(f"http://slowwly.robertomurray.co.uk/"
                        "delay/3000/url/{url}")

    # Get the text of the response
    page = resp.text

    # Cache the result with an expiration time of 10 seconds
    r.setex(url, 10, page)

    return page

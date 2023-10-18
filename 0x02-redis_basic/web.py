#!/usr/bin/env python3
""" Redis Module Cache and tracking """

from functools import wraps
import redis
import requests
from typing import Callable

# Create a Redis client instance
redis_ = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator for counting requests and caching content

    Args:
        method (Callable): The function to be decorated.

    Returns:
        Callable: Decorated function.
    """

    @wraps(method)
    def wrapper(url):
        """Wrapper function for counting and caching

        Args:
            url (str): The URL to fetch content from.

        Returns:
            str: The HTML content of the URL.
        """
        # Increment the count for the URL
        redis_.incr(f"count:{url}")

        # Check if the content is already cached in Redis
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode("utf-8")

        # Fetch HTML content from the URL
        html = method(url)

        # Cache the HTML content with a 10-second expiration
        redis_.setex(f"cached:{url}", 10, html)

        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Obtain the HTML content of a URL using caching and counting requests.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        str: The HTML content of the URL.
    """
    req = requests.get(url)
    return req.text

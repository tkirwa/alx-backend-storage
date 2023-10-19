#!/usr/bin/env python3
"""
Create a web cache
"""
import redis
import requests

# Create a connection to the Redis server
rc = redis.Redis()


def get_page(url: str) -> str:
    """
    Get a page and cache value.
    Args:
        url (str): The URL to get the page from.
    Returns:
        str: The HTML content of the page.
    """
    # Check if the page is already in cache
    page = rc.get(url)

    # If the page is not in cache, send a GET request to the URL
    if not page:
        resp = requests.get(url)
        page = resp.text

        # Cache the result with an expiration time of 10 seconds
        rc.setex(url, 10, page)

        # Increment the count for this URL
        rc.incr(f"count:{url}")

    return page


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")

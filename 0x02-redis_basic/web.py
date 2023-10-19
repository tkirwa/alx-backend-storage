#!/usr/bin/env python3
"""Web Cache and Tracker using Redis with Decorators."""

import redis
import requests
from functools import wraps

# Initialize a connection to the Redis server
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)


def cache_and_track(url):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if the URL count key exists in Redis
            url_count_key = f"count:{url}"
            if redis_client.exists(url_count_key):
                # If it exists, increment the count
                redis_client.incr(url_count_key)
            else:
                # If it doesn't exist, set it and set an expiration time of
                #  10 seconds
                redis_client.setex(url_count_key, 10, 1)

            # Check if the URL content is cached in Redis
            cached_content = redis_client.get(url)
            if cached_content:
                return cached_content.decode("utf-8")

            # If not cached, fetch the HTML content from the URL
            response = requests.get(url)
            html_content = response.text

            # Cache the content with an expiration time of 10 seconds
            redis_client.setex(url, 10, html_content)

            return html_content

        return wrapper

    return decorator


@cache_and_track(
    "http://slowwly.robertomurray.co.uk"
)
def get_page(url: str) -> str:
    """Fetch HTML content from a URL and cache it with tracking."""
    pass


if __name__ == "__main__":
    # Example usage of the get_page function
    content = get_page(
        "http://slowwly.robertomurray.co.uk"
    )
    print(content)

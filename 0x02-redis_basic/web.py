#!/usr/bin/env python3
"""web module
"""
import redis
import requests

_redis = redis.Redis()
_redis.flushdb()


def get_page(url: str) -> str:
    # Check if the content is cached in Redis
    cached = _redis.get(f"cached:{url}")
    if cached:
        return cached.decode("utf-8")

    # Content is not cached, make an HTTP GET request
    response = requests.get(url, timeout=10)
    content = response.text

    # Increment access count for this URL
    _redis.incr(f"count:{url}")

    # Cache the content with an expiration time of 10 seconds
    _redis.setex(f"cached:{url}", 10, content)

    return content


if __name__ == "__main__":
    # Example usage
    url = "http://slowwly.robertomurray.co.uk"
    page_content = get_page(url)
    print(page_content)

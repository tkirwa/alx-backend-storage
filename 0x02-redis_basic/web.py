#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
    obtain the HTML content of a particular URL and returns it """
import redis
import requests

# Create a Redis client instance
r = redis.Redis()


def get_page(url: str) -> str:
    """Track how many times a particular URL was accessed in the key
    "count:{url}" and cache the result with an expiration time of 10 seconds"""
    # Increment the access count
    r.incr(f"count:{url}")

    # Check if the content is already cached
    cached_content = r.get(f"cached:{url}")
    if cached_content:
        # If cached, return the cached content
        return cached_content.decode("utf-8")

    # If not cached, fetch the content from the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the content with an expiration time of 10 seconds
    r.setex(f"cached:{url}", 10, html_content)

    return html_content


if __name__ == "__main__":
    # Example usage of the get_page function
    content = get_page("http://slowwly.robertomurray.co.uk")
    print(content)

import requests
import redis
from functools import wraps

# Create a Redis client
redis_client = redis.Redis()


def track_url_access_count(url):
    """Decorator to track URL access count and cache the result."""

    def decorator(func):
        @wraps(func)
        def wrapper(url):
            # Create a key for counting URL accesses
            count_key = f"count:{url}"

            # Increment the access count
            redis_client.incr(count_key)

            # Check if the URL content is cached
            cached_content = redis_client.get(url)
            if cached_content:
                return cached_content.decode('utf-8')

            # Fetch the content from the URL
            response = requests.get(url)
            content = response.text

            # Cache the content with an expiration time of 10 seconds
            redis_client.setex(url, 10, content)

            return content

        return wrapper

    return decorator


@track_url_access_count("http://slowwly.robertomurray.co.uk/delay/5000/url/1")
def get_page(url: str) -> str:
    return requests.get(url).text


if __name__ == "__main__":
    # Test the get_page function
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/1"
    content = get_page(url)
    print(content)

    # Get the access count for the URL
    access_count = redis_client.get(f"count:{url}").decode('utf-8')
    print(f"Access Count for {url}: {access_count}")

import redis
import requests

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


def get_page(url: str) -> str:
    # Check if the URL count key exists in Redis
    url_count_key = f"count:{url}"
    if redis_client.exists(url_count_key):
        # If it exists, increment the count
        redis_client.incr(url_count_key)
    else:
        # If it doesn't exist, set it and set an expiration time of 10 seconds
        redis_client.setex(url_count_key, 10, 1)

    # Check if the URL content is cached in Redis
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    # If not cached, fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the content with an expiration time of 10 seconds
    redis_client.setex(url, 10, html_content)

    return html_content

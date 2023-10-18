##  0x02. Redis Basic (Back-end | Redis)
This project contains Python code that demonstrates how to use Redis for various basic operations, including storing and retrieving data, implementing a simple cache, and tracking function calls.

## Requirements

- Python 3.7
- `pycodestyle` style (version 2.5)
- [Redis](https://redis.io/) installed
- Python Redis Library (installed via `pip3 install redis`)

## Installation

To install Redis on Ubuntu 18.04, use the following commands:

```bash
sudo apt-get -y install redis-server
```

```bash
pip3 install redis
```

```bash
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Tasks

### 0. Writing strings to Redis

In this task, we create a `Cache` class that allows us to store data in Redis and generate random keys. The `store` method is used for this purpose.

#### Usage:

```python
import redis
Cache = __import__('exercise').Cache

cache = Cache()
data = b"hello"
key = cache.store(data)
print(key)
```

### 1. Reading from Redis and recovering the original type

This task involves creating a `get` method that retrieves data from Redis and allows for type conversion. Additionally, we implement `get_str` and `get_int` methods for automatic type conversion.

### 2. Incrementing values

In this task, we create a `count_calls` decorator that counts how many times methods of the `Cache` class are called.

#### Usage:

```python
Cache = __import__('exercise').Cache
cache = Cache()
cache.store(b"first")
print(cache.get(cache.store.__qualname__))
cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
```

### 3. Storing lists

This task involves implementing a `call_history` decorator to store the history of inputs and outputs for a particular function.

#### Usage:

```python
Cache = __import__('exercise').Cache
cache = Cache()

s1 = cache.store("first")
s2 = cache.store("second")
s3 = cache.store("third")

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)
```

### 4. Retrieving lists

In this task, we implement a `replay` function to display the history of calls of a particular function.

#### Usage:

```python
cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
```

### 5. Implementing an expiring web cache and tracker (Advanced)

In this advanced task, a `get_page` function is implemented to obtain the HTML content of a URL using the `requests` module. It also tracks how many times a particular URL was accessed and caches the result with an expiration time of 10 seconds.

To test this task, create a separate file named `web.py`.

## Repository

- GitHub repository: [alx-backend-storage](https://github.com/tkirwa/alx-backend-storage)
- Directory: 0x02-redis_basic
- File: exercise.py (for tasks 0-4), web.py (for task 5)

Make sure to replace `yourusername` in the GitHub repository link with your actual GitHub username or the organization where the project is hosted. This `README.md` provides an overview of the project, its requirements, installation instructions, and how to use the provided code for each task.
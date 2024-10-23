#!/usr/bin/env python3
"""
A script that does some Redis stuff with a python class and
some functions.
"""

import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    Decorator that counts how many times a URL is accessed.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        r.incr(f"count:{url}")
        cached_content = r.get(f"cached:{url}")
        if cached_content:
            return cached_content.decode('utf-8')
        content = method(url)
        r.setex(f"cached:{url}", 10, content)
        return content
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Fetches the content of a url
    """
    response = requests.get(url)
    return response.text

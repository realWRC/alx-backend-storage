#!/usr/bin/env python3
"""
A script that does some Redis stuff with a python class and
some functions.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Defines the cache class for caching with Redis
    """

    def __init__(self):
        """
        Initialises the Redis client and flushes the cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

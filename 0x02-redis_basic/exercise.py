#!/usr/bin/env python3
"""
A script that does some Redis stuff with a python class and
some functions.
"""

import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self,
            key: str,
            fn: Optional[Callable[[bytes], Union[str, int, bytes]]] = None)\
            -> Optional[Union[str, int, bytes]]:
        """
        Retrieve data from Redis
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

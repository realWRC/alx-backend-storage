#!/usr/bin/env python3
"""
A script that does some Redis stuff with a python class and
some functions.
"""

import redis
import uuid
from functools import wraps
from typing import Union, Callable, TypeVar, Optional, overload

T = TypeVar('T')


def count_calls(method: Callable) -> Callable:
    """
    Tracks number of calls made to method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Returns a method after incrementation of its call
        counter
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @overload
    def get(self, key: str) -> Optional[bytes]:
        ...

    @overload
    def get(self, key: str, fn: Callable[[bytes], T]) -> Optional[T]:
        ...

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None)\
            -> Optional[Union[bytes, T]]:
        """
        Retrieve data from Redis
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string from Redis using a key.
        """
        return self.get(key, fn=lambda s: s.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer from Redis using a key.
        """
        return self.get(key, fn=int)

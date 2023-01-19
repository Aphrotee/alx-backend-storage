#!/usr/bin/env python3

"""
This module provides the class Cache
"""

import redis
import uuid
import typing
from typing import Union, Optional


class Cache:
    """
    Cache class
    """
    def __init__(self) -> None:
        """
        initialize class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid),
        store the input data in Redis using the random key and return the key.
        """
        id: str = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self,
            key: str,
            fn: Optional[
                        typing.Callable[[bytes],
                                        Union[str, bytes, int, float]]
                    ]) ->\
            Union[str, bytes, int, float]:
        """
        This method retrieves data from the Redis server.
        """
        val = self._redis.get(key)
        if val is None:
            return None
        if fn is not None:
            val = fn(val)
        return val

    def get_str(self, b: bytes) -> str:
        """ Retreives string from the Redis server """
        def dec(b: bytes) -> str:
            """ Bytes to string conversion """
            return b.decode('utf-8')
        return self.get(b, dec)

    def get_int(self, b: bytes) -> int:
        """ Retreives integer from the Redis server """
        def dint(b: bytes) -> int:
            """ Bytes to integer conversion """
            return int(b)
        return self.get(b, dint)

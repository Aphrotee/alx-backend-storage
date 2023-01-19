#!/usr/bin/env python3

"""
This module provides the class Cache
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class
    """
    def __init__(self) -> None:
        """
        initialize class
        """
        self._redis = redis.Redis()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid),
        store the input data in Redis using the random key and return the key.
        """
        id: str = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

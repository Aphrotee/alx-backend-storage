#!/usr/bin/env python3

"""
This module provides the class Cache
"""

from functools import wraps
import redis
import uuid
import typing
from typing import Union, Optional


def count_calls(method: typing.Callable) -> typing.Callable:
    """
    This is a decorator that takes a single method
    Callable argument and returns a Callable
    """

    @wraps(method)
    def count(self, *args, **kwargs) -> typing.Callable:
        """ Counts the number of times the input method has been called
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return count


def call_history(method: typing.Callable) -> typing.Callable:
    """
    This decorator saves the call history of the store method
    """
    input = method.__qualname__ + ":inputs"
    output = method.__qualname__ + ":outputs"

    @wraps(method)
    def push(self, *args, **kwargs) -> typing.Callable:
        """
        This function push onto list `input` on the redis server
        """
        self._redis.rpush(input, str(args))
        out = method(self, *args, **kwargs)
        self._redis.rpush(output, str(out))
        return out
    return push


def replay(method: typing.Callable) -> None:
    """
    This function display the history of calls of a particular function.
    """
    r = redis.Redis()
    input = r.lrange(method.__qualname__ + ':inputs', 0, -1)
    output = r.lrange(method.__qualname__ + ':outputs', 0, -1)
    history = dict(zip(input, output))
    print('{} was called {} times'.format(method.__qualname__, len(history)))
    for keys, values in history.items():
        print('{}(*{}) -> {}'.format(method.__qualname__,
                                     keys.decode('utf-8'),
                                     values.decode('utf-8')))


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

    @count_calls
    @call_history
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
                    ] = None) ->\
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

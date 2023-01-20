#!/usr/bin/env python3

"""
This module provides the class Cache
"""

from functools import wraps
import redis
import requests
import requests_html
import typing


def counter(method: typing.Callable):
    """
    Counts the calls to the input method
    """

    @wraps(method)
    def count(self, url: str, *args, **kwargs) -> typing.Callable:
        """
        Caches the counts of visits to url
        """
        key = 'count:' + url
        self._redis.incr(key)
        self._redis.expire(key, 10)
        return counter(url, *args, **kwargs)
    return count


class Cache:
    """
    This class queries a webpage and monitors the number of visits to it
    """

    def __init__(self):
        """
        Initialize class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @counter
    def get_page(self, url: str) -> str:
        """
        This function ses the requests module to obtain
        the HTML content of a particular URL and returns it
        """
        response = requests.get(url)
        return response.text


if __name__ == '__main__':
    url = 'http://www.google.com'
    cache = Cache()
    print(cache)
    cache.get_page(url)

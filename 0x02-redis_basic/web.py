#!/usr/bin/env python3

"""
This module provides the class Cache
"""

from functools import wraps
import redis
import requests

def counter(method):
    """
    Counts the calls to the input method
    """
    @wraps(method)
    def count(self, url: str, *args, **kwargs):
        """
        Caches the counts of visits to url
        """
        key = 'count:' + url
        self._redis.incr(key)
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

    @counter
    def get_page(url: str) -> str:
        """
        This function ses the requests module to obtain
        the HTML content of a particular URL and returns it
        """
        pass
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()


replay(cache.store)
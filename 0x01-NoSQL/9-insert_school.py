#!/usr/bin/python3

"""
This module provides the function `insert_school`
"""


def insert_school(mongo_collection, **kwargs):
    """
    This is a funciton that inserts a new
    document in a collection base on kwargs
    """
    if mongo_collection is None or kwargs == {} or kwargs is None:
        return
    return mongo_collection.insert_one(kwargs)

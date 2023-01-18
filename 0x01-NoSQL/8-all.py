#!/usr/bin/python3

"""
This module provides the function `list_all`
"""


def list_all(mongo_collection):
    """
    Lists all the documments in a collection
    """
    if mongo_collection is None or not mongo_collection.count():
        return []
    return mongo_collection.find()

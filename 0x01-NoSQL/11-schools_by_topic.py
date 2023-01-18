#!/usr/bin/python3


"""
This module provides the function schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    This is a function that returns the list of schools having a specific topic
    """
    if mongo_collection is None:
        return
    return mongo_collection.find({"topics": topic})

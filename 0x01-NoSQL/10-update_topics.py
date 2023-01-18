#!/usr/bin/env python3

"""
This module provides the function update_topics
"""


def update_topics(mongo_collection, name, topics):
    """
    This is a function that  changes all
    topics of a school document based on the name
    """
    if mongo_collection is None:
        return
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

#!/usr/bin/env python3

"""
This module provides the function top_students
"""


def top_students(mongo_collection):
    """
    This function returns all students sorted by average score
    """
    if mongo_collection is None:
        return
    topStudents = mongo_collection.aggregate([{'$project': {
        "name": "$name",
        "averageScore": {
            "$avg": {
                "$avg": "$topics.score"
                }
            }
        }},
        {
            "$sort": {"averageScore": -1}
        }])
    return topStudents

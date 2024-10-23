#!/usr/bin/env python3
"""
Module with some python code to do some narly stuff
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    """
    students = mongo_collection.aggregate([
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
    return list(students)

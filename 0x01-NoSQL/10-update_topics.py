#!/usr/bin/env python3
"""
Module with some python code to do some narly stuff
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the name.
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

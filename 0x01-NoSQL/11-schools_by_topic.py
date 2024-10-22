#!/usr/bin/env python3
"""
Module with some python code to do some narly stuff
"""


def schools_by_topic(mongo_collection, topic):
    """
    Findw and returnw a list of schools that have a specific topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)

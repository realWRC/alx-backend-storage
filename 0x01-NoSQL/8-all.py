#!/usr/bin/env python3
"""
Module with some python code to do some narly stuff
"""

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection
    """
    if not mongo_collection:
        return []
    docs = list(mongo_collection.find())
    return docs

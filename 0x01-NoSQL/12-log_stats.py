#!/usr/bin/env python3
"""
Module with some python code to do some narly stuff
"""

from pymongo import MongoClient


def log_stats():
    """
    Accesses and provides stats on Nginx logs in MongoDB
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    collection = db.nginx

    totalLogs = collection.count_documents({})
    print(f"{totalLogs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    status_check_count = collection.count_documents(
            {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()

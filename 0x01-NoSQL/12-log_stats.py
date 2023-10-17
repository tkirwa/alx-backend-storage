#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Display some stats about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status_check = mongo_collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    nginx_collection = logs_db.nginx
    log_stats(nginx_collection)

#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to the MongoDB server running on localhost at port 27017
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the 'logs' database and the 'nginx' collection
    nginx_collection = client.logs.nginx

    # Retrieve the number of documents (logs) in the 'nginx' collection
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    # List of HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')

    # Count the number of documents with each method
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'    method {method}: {count}')

    # Count the number of documents with method=GET and path=/status
    status_check = nginx_collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f'{status_check} status check')

#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    # Connect to the MongoDB server running on localhost.
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Access the 'nginx' collection within the 'logs' database.
    nginx_collection = client.logs.nginx

    # Count the total number of logs in the collection.
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    # Define a list of HTTP methods to analyze.
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    # Count and print the number of documents for each method.
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    # Count the number of logs with a specific method and path.
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')

    # Use aggregation to find the top 10 IPs with the highest counts.
    top_ips = nginx_collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    # Print the top 10 IPs and their counts.
    print("IPs:")
    for top_ip in top_ips:
        ip = top_ip.get("ip")
        count = top_ip.get("count")
        print(f'\t{ip}: {count}')

# 0x01. NoSQL (Back-end | NoSQL | MongoDB)

This project involves working with MongoDB, a NoSQL database, and PyMongo, the Python driver for MongoDB. The project includes several tasks that require writing Python scripts to interact with a MongoDB database.

## Task 0: List all databases
**File:** `0-list_databases`

This script lists all databases in the MongoDB instance.

## Task 1: Create a database
**File:** `1-use_or_create_database`

This script creates or uses the database `my_db`.

## Task 2: Insert document
**File:** `2-insert`

This script inserts a document in the `school` collection with an attribute `name` set to "Holberton school".

## Task 3: All documents
**File:** `3-all`

This script lists all documents in the `school` collection.

## Task 4: All matches
**File:** `4-match`

This script lists all documents in the `school` collection where the `name` attribute is "Holberton school".

## Task 5: Count
**File:** `5-count`

This script displays the number of documents in the `school` collection.

## Task 6: Update
**File:** `6-update`

This script adds a new attribute, `address`, with the value "972 Mission street" to all documents in the `school` collection where the `name` attribute is "Holberton school".

## Task 7: Delete by match
**File:** `7-delete`

This script deletes all documents in the `school` collection where the `name` attribute is "Holberton school".

## Task 8: List all documents in Python
**File:** `8-all.py`

This Python script defines a function `list_all(mongo_collection)` that lists all documents in a given collection.

## Task 9: Insert a document in Python
**File:** `9-insert_school.py`

This Python script defines a function `insert_school(mongo_collection, **kwargs)` to insert a new document in a collection based on keyword arguments.

## Task 10: Change school topics
**File:** `10-update_topics.py`

This Python script defines a function `update_topics(mongo_collection, name, topics)` to change the topics of a school document based on the name.

## Task 11: Where can I learn Python?
**File:** `11-schools_by_topic.py`

This Python script defines a function `schools_by_topic(mongo_collection, topic)` that returns a list of schools having a specific topic.

## Task 12: Log stats
**File:** `12-log_stats.py`

This script provides statistics about Nginx logs stored in MongoDB, including the number of documents, HTTP methods, and the number of status checks.

## Task 13: Regex filter (Advanced)
**File:** `100-find`

This script lists all documents in the `school` collection where the `name` attribute starts with "Holberton."

## Task 14: Top students (Advanced)
**File:** `101-students.py`

This script defines a function `top_students(mongo_collection)` that returns all students sorted by average score.

## Task 15: Log stats - new version (Advanced)
**File:** `102-log_stats.py`

This script enhances the log statistics script to include the top 10 most present IPs in the Nginx logs.

**Note:** To run these scripts, ensure that you have MongoDB and PyMongo installed in your environment, and you can use the `mongo` command-line tool to interact with the database.

For each task, you can execute the corresponding script as mentioned in the task descriptions to perform the required actions.

Feel free to reach out if you have any questions or need further assistance with these tasks!

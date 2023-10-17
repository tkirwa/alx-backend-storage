#!/usr/bin/env python3
"""
Top students
Write a Python function that returns all students sorted by average score
"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Get a list of students sorted by average score.

    Args:
        mongo_collection: A pymongo collection object representing 
        the students' data.

    Returns:
        List of students sorted by average score in descending order.
    """
    students = list(mongo_collection.find())

    for student in students:
        topics = student.get('topics', [])
        total_score = 0
        for topic in topics:
            total_score += topic.get('score', 0)
        average_score = total_score / len(topics) if len(topics) > 0 else 0
        student['averageScore'] = average_score

    sorted_students = sorted(students, key=lambda x: x['averageScore'],
                             reverse=True)
    return sorted_students

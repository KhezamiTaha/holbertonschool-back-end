#!/usr/bin/python3
"""
This script will use the REST API to return information
about a given employee's TODO list progress.
"""
import json
import requests


def TODO_REQUESTS():
    """
    extend your Python script to export data in the JSON format
    """
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users"
    ).json()

    data = {
        user["id"]: [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
            for task in todos
            if task["userId"] == user["id"]
        ]
        for user in users
    }

    with open(f"todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    TODO_REQUESTS()

#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys


def export_to_json(employee_id):
    # Fetch employee data
    employee = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    employee_name = employee.get("username")

    # Fetch employee's tasks
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        ).json()

    # Prepare data in JSON format
    datta = {
        f"{employee_id}": [{
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        } for task in todos]
    }

    # Write data to JSON file
    with open(f"{employee_id}.json", "w") as jsonfilee:
        json.dump(datta, jsonfilee)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    export_to_json(employee_id)

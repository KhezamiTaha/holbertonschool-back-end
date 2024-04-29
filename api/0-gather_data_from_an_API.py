#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys


def TO_DO(employee_id):
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    Response_object = requests.get(api_url)
    employee_todos_list = Response_object.json()
    employee = requests.get(
                f"https://jsonplaceholder.typicode.com/users/{employee_id}"
                ).json()
    employee_name = employee.get("name")
    completed_tasks = []
    for task in employee_todos_list:
        if task["completed"]:
            completed_tasks.append(task["title"])
    print(f"Employee {employee_name} is done with tasks"
          f"({len(completed_tasks)}/{len(employee_todos_list)}):")

    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    employee_id = sys.argv[1]
    TO_DO(employee_id)

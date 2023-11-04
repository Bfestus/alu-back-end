#!/usr/bin/python3

import json

def export_tasks_to_json(tasks):
    """
    Export tasks to a JSON file for all employees.

    :param tasks: Dictionary containing tasks for all employees
    :type tasks: dict
    """
    # Write the dictionary to a JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(tasks, json_file, indent=2)

def organize_tasks_by_employee(tasks):
    """
    Organize tasks by employee.

    :param tasks: List of tasks
    :type tasks: list
    :return: Dictionary containing tasks organized by employee
    :rtype: dict
    """
    organized_tasks = {}

    for task in tasks:
        user_id = task.get("user_id", "")
        username = task.get("username", "")

        if user_id not in organized_tasks:
            organized_tasks[user_id] = []

        task_info = {
            "username": username,
            "task": task.get("title", ""),
            "completed": task.get("completed", False)
        }

        organized_tasks[user_id].append(task_info)

    return organized_tasks

if __name__ == "__main__":
    # Example usage with tasks for multiple users
    tasks = [
        {"user_id": "123", "title": "Task 1", "completed": True, "username": "john_doe"},
        {"user_id": "123", "title": "Task 2", "completed": False, "username": "john_doe"},
        {"user_id": "456", "title": "Task 3", "completed": True, "username": "jane_smith"},
        # Add more tasks as needed
    ]

    organized_tasks = organize_tasks_by_employee(tasks)
    export_tasks_to_json(organized_tasks)

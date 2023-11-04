#!/usr/bin/python3

import json

def export_tasks_to_json(user_id, tasks):
    """
    Export tasks to a JSON file based on user ID.

    :param user_id: User ID
    :type user_id: str
    :param tasks: List of tasks
    :type tasks: list
    """
    # Create a dictionary to store tasks for the user
    user_tasks = {user_id: []}

    # Iterate through tasks and append relevant information to the dictionary
    for task in tasks:
        task_info = {
            "task": task.get("title", ""),
            "completed": task.get("completed", False),
            "username": task.get("username", "")
        }
        user_tasks[user_id].append(task_info)

    # Write the dictionary to a JSON file
    filename = f"{user_id}.json"
    with open(filename, "w") as json_file:
        json.dump(user_tasks, json_file, indent=2)

if __name__ == "__main__":
    # Example usage
    user_id = "123"
    tasks = [
        {"title": "Task 1", "completed": True, "username": "john_doe"},
        {"title": "Task 2", "completed": False, "username": "john_doe"},
        # Add more tasks as needed
    ]

    export_tasks_to_json(user_id, tasks)

#!/usr/bin/python3
"""
This script fetches and displays the TODO list
"""

import requests
import sys

def fetch_todo_list_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
        The ID of the employee whose TODO list progress is to be fetched.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user data from the API
    user_response = requests.get(user_url)
    # Fetch TODO list data for the specific user from the API
    todos_response = requests.get(todos_url)

    # Check if API requests were successful
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        return

    # Parse JSON responses
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Display employee TODO list progress
    print(f"Employee {user_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        try:
            # Parse employee ID from the command-line argument
            employee_id = int(sys.argv[1])
            # Fetch and display TODO list progress for the given employee ID
            fetch_todo_list_progress(employee_id)
        except ValueError:
            print("Error: Invalid employee ID. Please provide a valid integer.")


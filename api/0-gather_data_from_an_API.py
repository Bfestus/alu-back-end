#!/usr/bin/python3
"""
This script fetches and displays the TODO list
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID.

    :param employee_id: Integer representing the employee ID.
    """
    # Base URL for the JSONPlaceholder API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Endpoint for user details
    user_endpoint = f'{base_url}/users/{employee_id}'

    # Endpoint for user's TODO list
    todo_endpoint = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch user details
        user_response = requests.get(user_endpoint)  # Fix variable name
        u_data = user_response.json()

        # Fetch user's TODO list
        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()

        # Calculate TODO progress
        t_tasks = len(todo_data)
        c_tasks = sum(task['completed'] for task in todo_data)

        # Display progress information
        print(f"Employee Name: {u_data.get('name', 'Unknown')} ({c_tasks}/{t_tasks}):")  # Correct Employee name

        # Display titles of completed tasks
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Get employee ID from the command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to get and display employee TODO list progress
    get_employee_todo_progress(employee_id)

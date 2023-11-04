#!/usr/bin/python3
"""
This script fetches and displays the TODO list and exports it to a CSV file.
"""

import sys
import requests
import csv


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
        user_response = requests.get(user_endpoint)
        u_data = user_response.json()

        # Fetch user's TODO list
        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()

        # Display progress information
        employee_name = u_data.get('username', 'Unknown')
        print(f"Employee Name: {employee_name}")

        # Export tasks to CSV
        csv_file_name = f"{employee_id}.csv"
        with open(csv_file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow
            (["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            # Write each task to the CSV file
            for task in todo_data:
                task_completed_status = "Completed" if task['completed'] 
                                                    else "Not Completed"
                csv_writer.writerow([
                    employee_id,
                    employee_name,
                    task_completed_status,
                    task['title']
                ])

                # Display titles of completed tasks
                if task['completed']:
                    print(f"\t{task['title']}")

        print(f"Tasks exported to {csv_file_name}")

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

    # Call the function to get and display employee TODO list
    get_employee_todo_progress(employee_id)

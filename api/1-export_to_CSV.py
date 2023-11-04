#!/usr/bin/python3
"""
script fetches and displays the TODO list and exports it to a CSV file.
"""

import requests
import sys
import csv

def fetch_todo_list_progress(employee_id):
    """
    Fetches TODO list progress for a given employee ID and exports data in CSV format.

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

    # Prepare data for CSV export
    csv_data = []
    for task in todos_data:
        task_completed_status = "True" if task['completed'] else "False"
        csv_row = [user_data['id'], user_data['username'], task_completed_status, task['title']]
        csv_data.append(csv_row)

    # Export data to CSV file
    file_name = f"{user_data['id']}.csv"
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csvwriter.writerows(csv_data)

    print(f"Data exported to {file_name}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        try:
            # Parse employee ID from the command-line argument
            employee_id = int(sys.argv[1])
            # Fetch TODO list progress for the given employee ID and export data to CSV
            fetch_todo_list_progress(employee_id)
        except ValueError:
            print("Error: Invalid employee ID. Please provide a valid integer.")


# Name: Peter Ddamulira
# Assignment: Module 9 - APIs
# Description:
# This program connects to the JSONPlaceholder API, tests the connection,
# displays the raw response, and then displays formatted user information.

import requests


def display_users(users):
    """Display selected user information in a readable format."""
    print("\nFormatted Response")
    print("------------------")

    for user in users:
        print(f"Name: {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Email: {user['email']}")
        print(f"City: {user['address']['city']}")
        print("-" * 35)


api_url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(api_url, timeout=10)

    print("JSONPlaceholder API Connection Test")
    print("-----------------------------------")
    print("Status code:", response.status_code)

    response.raise_for_status()

    print("\nRaw Response")
    print("------------")
    print(response.text)

    users = response.json()
    display_users(users)

except requests.exceptions.RequestException as error:
    print("An API request error occurred:", error)
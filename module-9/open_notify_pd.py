# Name: Peter Ddamulira
# Assignment: Module 9 - APIs
# File: open_notify_pd.py
# Description:
# This program connects to the Open Notify API, tests the connection,
# retrieves the current astronaut data, and displays formatted results.

import requests


def display_astronauts(api_data):
    """Display each astronaut's name and spacecraft."""

    print("\nCurrent Astronauts in Space")
    print("---------------------------")

    for person in api_data["people"]:
        print(f"{person['name']} is aboard the {person['craft']}.")

    print(f"\nTotal number of people in space: {api_data['number']}")


def main():
    """Connect to the API and process the returned information."""

    api_url = "http://api.open-notify.org/astros.json"

    try:
        response = requests.get(api_url, timeout=10)

        # Test and display the API connection.
        print("Open Notify API Connection Test")
        print("-------------------------------")
        print(f"Status code: {response.status_code}")

        # Raise an exception if the request was unsuccessful.
        response.raise_for_status()

        # Convert the JSON response into a Python dictionary.
        astronaut_data = response.json()

        # Display the formatted astronaut information.
        display_astronauts(astronaut_data)

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: The program could not connect to the API.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")

    except (KeyError, ValueError) as error:
        print(f"Error processing the API data: {error}")


if __name__ == "__main__":
    main()
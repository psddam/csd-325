# Name: Peter Ddamulira
# Assignment: Module 4 - Sitka Highs and Lows
# Description:
# This program reads Sitka weather data from a CSV file and allows the user
# to choose whether to display high temperatures, low temperatures, or exit.
# Changes made:
# 1. Added a menu for Highs, Lows, and Exit.
# 2. Added low temperature graph in blue.
# 3. Added loop so the menu continues until user exits.
# 4. Added exit message.

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

# Read weather data from CSV file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)


def plot_highs():
    """Displays a graph of Sitka high temperatures."""
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def plot_lows():
    """Displays a graph of Sitka low temperatures."""
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


# Main menu loop
while True:
    print("\nSitka Weather Program")
    print("----------------------")
    print("Please select an option:")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")

    choice = input("SPD: ").lower()

    if choice == "1" or choice == "highs":
        plot_highs()
    elif choice == "2" or choice == "lows":
        plot_lows()
    elif choice == "3" or choice == "exit":
        print("Thank you for using the Sitka Weather Program. Goodbye!")
        sys.exit()
    else:
        print("Invalid option. Please enter Highs, Lows, or Exit.")
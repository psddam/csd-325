# Name: Peter Ddamulira
# Assignment: Module 1 - On the Wall
# Description:
# This program asks the user how many bottles of beer are on the wall.
# The number is passed to a function that counts down to 1.
# After the countdown ends, the main program reminds the user to buy more beer.

def countdown_bottles(bottles):
    """Counts down bottles of beer from the user number to 1."""

    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall.")
        print(f"{bottles} bottles of beer.")
        print("Take one down, pass it around.")
        bottles -= 1
        print(f"{bottles} bottle(s) of beer on the wall.\n")

    if bottles == 1:
        print("1 bottle of beer on the wall.")
        print("1 bottle of beer.")
        print("Take it down, pass it around.")
        print("No more bottles of beer on the wall.\n")


# Main program
print("Welcome to the Bottles of Beer Countdown Program")
print("------------------------------------------------")

# Get user input
num_bottles = int(input("How many bottles of beer are on the wall? "))

# Call function
countdown_bottles(num_bottles)

# Final reminder from main program
print("Time to buy more beer!")
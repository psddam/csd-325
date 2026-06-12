# Name: Peter Ddamulira
#Date: June 12, 2026
# Assignment: Module 2 - Documented Debugging
# Description:
# This program asks the user for the number of bottles and passes that number
# to a function that counts down until one bottle remains.

def countdown_bottles(bottles):
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


print("Welcome to the Bottles of Beer Countdown Program")
num_bottles = int(input("How many bottles of beer are on the wall? "))

countdown_bottles(num_bottles)

print("Time to buy more beer!")
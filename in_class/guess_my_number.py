#!/usr/bin/env python3

###
# Nathaniel Watson
# 2018-06-21
# De Anza College Academy
###

"""
A random number between 1 and 1000 is chosen, and the user must try to guess what that number is
in the least number of guesses as possible. This script demonstrates the use of a "while loop" that
runs forever until explicitly broken out of when the condition is right using the "break" keyword. 
This script also demonstrates:

    - Generating a random integer within a specified range.
    - Getting user input using the "input()" function, and storing the value into a variable. 
    - Converting a string representation of a number to an interger data type using the "int()" 
      built-in function. 
    - A compound "if" statement consisting of an "elif" block and an "else" block. 
"""

from random import randint

# Get a random integer between 1 and 100:
my_num = randint(1, 100)
# Track how many guesses the user makes:
guesses = 0
while True:
    guesses = guesses + 1
    user_num = input("Pick a number between 1 and 100: ") 
    #user_num is currently a string; need to convert to an integer.
    user_num = int(user_num)
    if user_num > my_num:
        print("Lower")
    elif user_num < my_num:
        print("Higher")
    else:
        print("That's it! {} is my number. You won in {} guesses".format(my_num, guesses))
        # Need to get out of the while loop now that the game is over, otherwise it'll run forever!
        break



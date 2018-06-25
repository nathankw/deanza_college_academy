#!/usr/bin/env python3

###
# Nathaniel Watson
# 2018-06-21
# De Anza College Academy
###


"""
The following exercise is to practice calling functions. The program demonstrates

  - Writing functions that take arguments and return values.
  - Working with list arguments.
  - Using Python's built-in min() and max() functions.
  - Getting a string representation of an integer using Python's built-in str() function.

Below are the original instructions that were given in class. Below the instructions are the
solutions - the code.  Please compare with the code you generated and run this in IDLE.

INSTRUCTIONS:

For this exercise, pair up. Open up IDLE create create a new file.
Save your file as calling_functions_demo.py.  Both you and your partner need to
each write the code in your own file, but work together in pairs.

1) Write a function called minimum that accepts a list argument and reports the
   smallest number in a list:

2) Write a function called maximum that accepts a list argument and reports the
   largest number in the list.

3) Write a function called min_max that accepts a list argument and calls the
   above functions.

   It should return a list of size two, where the first element is the result of
   calling the minimum function, and the second element is the result of calling
   the maximum function.

4) Run your program in IDLE

5) Call the min_max function, and assign the result to a variable.

5) Print the variable to the user with a custom message,
   i.e. "Here is your result".
"""

def minimum(numbers):
    min_num = min(numbers) # Calls Python's built-in min() function
    print("I found the minimum of your list to be " + str(min_num)) 
    return min_num

def maximum(numbers):
    max_num = max(numbers) # Calls Python's built-in max() function.
    print("I found the maximum of your list to be " + str(max_num))
    return max_num

def min_max(numbers):
    min_num = minimum(numbers)
    max_num = maximum(numbers)
    # Return both in a list object
    return [min_num, max_num]


x = [55, 47, 100, 103, 97, 58, 3, 21]
result = min_max(x)
print(result)






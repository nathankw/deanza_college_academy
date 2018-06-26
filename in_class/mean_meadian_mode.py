###
# Nathaniel Watson
# 2018-06-21
# De Anza College Academy
###

import math

def mean(numbers):
    """
    Calculates the mean of the provided list of numbers.
    """
    length = len(numbers)
    sum_numbers = sum(numbers)
    return sum_numbers/length

def median(numbers):
    """
    Calculates the median (middle value) in the provided list of numbers.
    Works for both even-sized and odd-sized lists.
    """
    numbers.sort()
    length = len(numbers)
    # We need to find out if the length is odd or even. If odd, then there is one number in the middle
    # i.e. [1, 2, 3].  2 is in the middle!
    #
    # But if the length is even, there are two middle numbers:
    # i.e. [1, 2, 3, 4] . 2 and 3 are both in the middle!
    #
    # % is an operator that gives you the remainder of division. If length is odd,
    # then (length % 2)
    # will have a non-zero remainder. If length is even, then (length % 2)
    # will have a remainder of 0.
    is_odd = length % 2
    if is_odd:
        # Imagine a test list of numbers being [1, 2, 3].
        # There is one middle number, 3.
        middle_position = length/2
        # This gives a fractional number of 1.5. Need to round down:
        middle_position = math.floor(middle_position)
        middle_number = numbers[middle_position]
    else:
        # length is even. Take the average of the two middle numbers.
        # Imagine a test list of numbers being [1, 2, 3, 4].
        # The middle two numbers are 2 and 3.
        middle_position_1 = int((length/2)) - 1  #Use int() since division gives a float, i.e. 1.0.
        middle_number_1 = numbers[middle_position_1]
        middle_position_2  = int(length/2) #Use int() since division gives a float, i.e. 1.0.
        middle_number_2 = numbers[middle_position_2]
        middle_number = mean([middle_number_1,middle_number_2])
    return middle_number

def mode(numbers):
    """
    Calculates the mode of the provided list of numbers. 
    The mode is the number that occurs most frequently in the list.
    The list will be sorted from least to greatest.
    Note that if there are any ties, the first in the set of ties is returned. 

    For example: if numbers is [1, 2, 2, 1], then this function returns 1. 
    If numbers is [1, 2, 3, 4], the the return value is 1. 
    If numbers is [100, 99, 100], then the return value is 100.
    """
    numbers.sort()
    freq_max = 1
    num = numbers[0]
    for i in set(numbers):
        # Get frequency of number i in list
        freq = numbers.count(i)
        if freq > freq_max:
            freq_max = freq
            num = i
    return num

def summary(numbers):
    """
    Calculates the mean, meadian, and mode of the provided list of numbers.
    """
    my_mean = mean(numbers)
    my_median = median(numbers)
    my_mode = mode(numbers)
    return [my_mean, my_median, my_mode]

if __name__ == "__main__":
    # Demo the program for use in IDLE:
    print("Welcome, lets get started. Let's calculate the mean, median, and mode of the numbers that you provide.")
    user_numbers = []
    print("Press enter to quit")
    while True:
       txt = input("Enter a number: ") 
       if not txt:
           break # User is done
       user_numbers.append(int(txt))
    results = summary(user_numbers)
    print("The results are in!")
    print("Mean: " + str(results[0]))
    print("Median: " + str(results[1]))
    print("Mode: " + str(results[2]))


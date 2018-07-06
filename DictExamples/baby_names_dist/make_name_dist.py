#!/usr/bin/env python3                                                                                 
                                                                                                       
###                                                                                                    
# Nathaniel Watson                                                                                     
# 2018-06-26                                                                                           
# De Anza College Academy                                                                              
###

"""
This program is good for practicing reading files and using Python dictionaries.

The top 100 most popular girl baby names of 2017 according to https://www.babycenter.com/top-baby-names-2017.html
were saved to a file, then shuffled in Python and 1000 random selection were made. Then, the same
was done for baby boy names. These two files can be found on GitHub at 
  https://github.com/nate086/deanza_college_academy/blob/master/IO/1000_baby_girl_names.txt
  https://github.com/nate086/deanza_college_academy/blob/master/IO/1000_baby_boy_names.txt
respectively.

The purpose of this program is to demonstrate how Python can be used to read one of those files
to create a distribution that tabulates the count that each baby name was seen in the file. The 
program also shows how to report the baby name with the greatest count.
"""

import operator
import os
import pdb
# Change to thumbdrive (assuming plugged in and set to drive D):
# os.chdir("D:")

# Open girl names file from GitHub. Download to same directory as this script.
#f = open("1000_baby_girl_names.txt", "r")
# Or use the boy names file:
f = open("1000_baby_boy_names.txt", "r")
d = {}
for line in f:
    line = line.strip()
    # Each line is now a baby name
    if line in d:
        # Name is already in the dictionary, so add one to the count.
        d[line] += 1
    else:
        # Name we have't seen yet, add it to the dictionary with an initial count of 1.
        d[line] = 1

# Calculate the most popular baby name:
def okay_solution(names):
    max_freq = 0
    max_name = ""
    for name in d:
        freq = d[name]
        if freq > max_freq:
            max_freq = freq
            max_name = name

def better_solution(names):
    names = names.items()
    sorted_items = sorted(names, key=operator.itemgetter(1), reverse=True)
    return sorted_items[0]
    
#max_name, max_freq = okay_solution(names=d) 
max_name, max_freq = better_solution(names=d)
print("The most popular name is: {} at a count of {}.".format(max_name, max_freq))
# For girls file, should get "The most popular name is: Serenity at a count of 20."
# For boys file, should get "The most popular name is: Elijah at a count of 18."

#!/usr/bin/env python3                                                                                 
                                                                                                       
###                                                                                                    
# Nathaniel Watson                                                                                     
# 2018-06-26                                                                                           
# De Anza College Academy                                                                              
###

"""
Demonstrates some basic concepts around Python's dictionary built-in data type. 
A dictionary object is used to construct a real-world example of a dictionary that 
translates words from English to French.
"""

d = {}

d["hi"] = "bonjour"
d["I"] = "je"
d["day"] = "jour"

print()
print("The keys in the dictionary (the English words) are:")
print( d.keys() )
print()

print("The values in the dictionary (the French words) are:")
print( d.values() )
print()

# How do you say hi in French?
print("Here's how you say 'hi' in French:")
print( d["hi"] )

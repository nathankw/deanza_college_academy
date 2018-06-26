#!/usr/bin/env python3                                                                                 
                                                                                                       
###                                                                                                    
# Nathaniel Watson                                                                                     
# 2018-06-26                                                                                           
# De Anza College Academy                                                                              
### 


"""
This program is good practice for the while loop.
It counts down from 10 before printing it's final last words.

For an exercise, try augmenting this program to play a sound in each iteration of the while loop,
and finally an explosion sound at the end of the program.
"""

import time

count = 10
print("Will self destruct in: ")
while count:
    if count == 3:
        print("Get out of here, quick!")
    print(count)
    count -= 1
    time.sleep(1) # sleep for 1 second
print("Boom!")

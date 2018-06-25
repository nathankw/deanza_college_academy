#!/usr/bin/env python3

###
# Nathaniel Watson
# 2018-06-21
# De Anza College Academy
###

"""
This program demonstrates the use of a while loop that terminates once the test condition becomes
false. It also demonstrates:

    - How to use a compound if statement containing the optional "elif" and "else" blocks.
    - How to use the "time" module (part of the Python Standard Library) to sleep (pause the script) 
      for some specified number of seconds.

We start out with 10 cookies. Each time the block in the while loop runs, one cookie is subtracted.
Eventually, there are 0 cookies left and the test condition becomes false, which terminates the
while loop.
"""

import time

cookies = 10
while cookies > 0:
    cookies = cookies - 1
    print("Have a cookie")
    if cookies > 1:
        print("There are {} cookies left.".format(cookies))
    elif cookies == 1:
        print("There is 1 cookie left.")
    else:
        print("There are no more cookies left, bye!")
    # Sleep (pause) for one second.
    time.sleep(1) 

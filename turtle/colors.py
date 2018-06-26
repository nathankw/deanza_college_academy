#!/usr/bin/env python3

###
# Nathaniel Watson
# 2018-06-26
# De Anza College Academy
###


"""
This program demonstrates the use of for-loops to create fascinating designs in turtle.
"""

import turtle

ANGLE = 80

turtle.speed(0) # Fastest
colors = ["red", "cyan", "teal", "gold", "purple"]
color_index = -1
for i in range(300):
        # The color will change in each iteration of the for-loop.
	color_index += 1
	color = colors[color_index]
	turtle.pencolor(color) # Change the drawing color
	if color_index == len(colors) -1:
	    color_index = -1
	turtle.forward(i)
	turtle.left(ANGLE)

# Q1) What happens when you set ANGLE to 90?  How about 45?

# Q2) Try changing the colors. 

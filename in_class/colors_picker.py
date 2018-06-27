#!/usr/bin/env python3

###
# Nathaniel Watson
# 2018-06-21
# De Anza College Academy
###


"""
 The colors that humans can detect are actually mixtures of varying intensities of red, green, and 
 blue. If you mix different intensities of red, green, and blue together, you can create any 
 color you want. You can experiment with varying amounts of red, green, and blue by using the 
 color picker at https://www.w3schools.com/colors/colors_rgb.asp. Try to adjust the values until
 you can get the desired color.

 Write a program that uses a dictionary to store the RGB values for the following colors:

  black
  blue
  green
  orange
  pink
  purple
  red
  white
  yellow

  Each key in the dictionary should be a color name, and the corresponding value should be a list
  of integers containing the RGB values, where the first elemment is the value for red, the second
  the value for green, and the third the value for blue. 

  You program should list all the color names that your program knows about and then ask the user 
  to pick one of them. Then, your program will tell the user the RGB values for that color.

  Extra challenges:
    1) Use a while loop to keep the program alive until the user is done inputting color names.
"""

colors = {}

colors["black"] = [0, 0, 0]
colors["white"] = [255, 255, 255]
colors["red"] = [255, 0, 0]
colors["green"] = [0, 255, 255]
colors["blue"] = [00, 0, 255]
colors["orange"] = [255, 165, 0]
colors["pink"] = [255, 192, 203]
colors["purple"] = [128, 0, 128]
colors["yellow"] = [255, 255, 0]

print("Welcome to the color picker!")
print("You can choose from any of the following {} colors:".format(len(colors)))
print( list(colors.keys()) )
print()

while True:
    user_color = input("What color would you like? ")
    if user_color == "":
       #Then user just hit the return key and nothing else, so end the program.
        break
    print(colors[user_color])


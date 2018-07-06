#!/usr/bin/env python

###
# Nathaniel Watson
# 2018-07-07
# De Anza College Academy
###

"""
Generates random, colorful dots in turtle.
"""

import random
import time
from tkinter import *
from tkinter.colorchooser import askcolor
import turtle as t


t.home()

def set_bg_col():
    rgb, hex_val = askcolor()
    print(hex_val)
    t.bgcolor(hex_val)

def set_pen_col():
    rgb, hex_val = askcolor()
    t.pencolor(hex_val)
    
#bg_btn = Button(text="Set background color", command=set_bg_col)
#bg_btn.pack()
#pen_btn = Button(text="Set pen color", command=set_pen_col)
#pen_btn.pack()
#mainloop()

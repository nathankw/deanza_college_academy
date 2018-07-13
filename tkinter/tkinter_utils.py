#!/usr/bin/env python

###
# Nathaniel Watson
# 2018-07-07
# De Anza College Academy
###

"""
Howdy
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

def set_happy_bg_pic(event):
    t.bgpic("../assets/images/Garfield-the-cat_thumb_300.gif")

def set_sad_bg_pic(event):
    t.bgpic("../assets/images/sad_cat_thumb_300.gif")

def save():
    """
    Saves the canvas to a Postscript file.
    """
    c = t.getcanvas(filename)
    if not filename.endswith(".ps"):
        filename += ".ps"
    c.postscript(file=filename)
    
bg_btn = Button(text="Set background color", command=set_bg_col)
bg_btn.pack()
pen_btn = Button(text="Set pen color", command=set_pen_col)
pen_btn.pack()

bg_happy_cat = Button(text="Happy")
bg_happy_cat.pack()
bg_happy_cat.bind("<Button-1>", set_happy_bg_pic)

bg_sad_cat = Button(text="Sad")
bg_sad_cat.pack()
bg_sad_cat.bind("<Button-1>", set_sad_bg_pic)
#mainloop()

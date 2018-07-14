#!/usr/bin/env python

###
# Nathaniel Watson
# 2018-07-12
# De Anza College Academy
###

"""
Intertwines turtle drawings with tkinter objects. Tkinter is a Python library for building
graphical user interfaces (GUIs). When you use turtle for drawing, you are actually using tkinter
behind the scenes. In this demo, we'll open up a turtle drawing area (which is actually a Canvas
object from tkinter), and add buttons and input boxes to enhance our user experience. 

In a Python shell (i.e. IDLE), import this file as follows:
    from tkinter_utils import *
"""

import random
import time
import tkinter
from tkinter.colorchooser import askcolor
import turtle as t


t.home() # Opens up the root window with a Canvas for drawing. 
         # The root window is our GUI that we'll draw on and add buttons to.

# The below functions are our event handlers for button clicks. They will be registered
# as callbacks when we make the buttons objects.

def set_bg_col():
    """
    Prompts the user to select a color that will be used for the background
    of the Canvas (drawing area). 
    """
    rgb, hex_val = askcolor()
    t.bgcolor(hex_val)

def set_pen_col():
    """
    Prompts the user to select a new drawing color.
    """
    rgb, hex_val = askcolor()
    t.pencolor(hex_val)

def set_bgpic_garfield(event):
    """
    Sets a background picture of Garfield.
    """
    t.bgpic("Garfield-the-cat_thumb_300.gif")

def set_bgpic_nature(event):
    """
    Sets a background picture of a pretty mountain alongside a lake. 
    """
    t.bgpic("mountain-lake_300px.gif")

def save(name):
    """
    Saves the art on the Canvas to a Postscript file. Unfortunately, there isn't a PDF option, and 
    you probably want to later convert your Postscript file to PDF format. 

    Args:
        name - The name of the Postscript file. If it doesn't end with a .ps extensions, 
               then this extension will be added. 
    """
    canvas = t.getcanvas()
    if not name.endswith(".ps"):
        name += ".ps"
    canvas.postscript(file=name)
    
bgcol_btn = tkinter.Button(text="Set background color", command=set_bg_col)
bgcol_btn.pack() # The pack() method Adds to button to the GUI

pencol_btn = tkinter.Button(text="Set pen color", command=set_pen_col)
pencol_btn.pack()

btn_garfield = tkinter.Button(text="Happy")
btn_garfield.pack()
btn_garfield.bind("<Button-1>", set_bgpic_garfield) # Button-1 is for left-click.

btn_nature = tkinter.Button(text="Nature")
btn_nature.pack()
btn_nature.bind("<Button-1>", set_bgpic_nature) 

if __name__ == "__main__":
    # Can't draw in turtle if in event loop
    tkinter.mainloop()


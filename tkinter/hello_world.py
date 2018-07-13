#!/usr/bin/env python3

###
# Nathaniel Watson
# 2018-07-12
# De Anza College Academy
###

import sys
from tkinter import *

root = Tk()
Label(root, text="Howdy there!").pack() # default pack side is TOP.
btn = Button(text="Click me!", command=sys.exit)
btn.pack()

def left_click(event):
    print("Okay, left click.")

def dbl_left_click(event):
    print("Double left, eh?")

btn2 = Button(text="Bind")
btn2.pack(expand=YES, fill=BOTH)
btn2.bind("<Button-1>", left_click)             # bind left mouse clicks
btn2.bind("<Double-1>", dbl_left_click)              # bind double-left clicks

#root.mainloop()

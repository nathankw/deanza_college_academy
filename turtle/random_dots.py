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
import turtle as t


def random_dots():
    t.hideturtle()
    t.speed(0)
    t.tracer(False)
    colors = ["red", "black", "blue", "yellow", "green", "pink", "purple", "orange"]
    wh = int(t.window_height()/2)
    ww = int(t.window_width()/1)
    while True:
        t.penup()
        t.color(random.choice(colors))
        random_h = random.randrange(-1 * wh, wh)
        random_w = random.randrange(-1 * ww, ww)
        t.begin_fill()
        t.goto(random_w, random_h)
        t.pendown()
        t.circle(10)
        t.end_fill()
        t.update()
        #time.sleep(0.09)

random_dots()
        

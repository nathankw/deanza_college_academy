#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# © 2018 The Board of Trustees of the Leland Stanford Junior University
# Nathaniel Watson
# nathankw@stanford.edu
###


import time
from sense_hat import SenseHat

sense = SenseHat()

# The default scroll speed is 0.1. The bigger the number, the faster the speed.


msg = "Howdy!"
#sense.show_message(msg)

w = (255, 255, 255)
r = (255, 0, 0)
b = (0, 0, 255)
y = (255, 255, 0)

#sense.show_message(msg, text_colour=red, back_colour=blue)
sense.clear()

# Make an arrow by setting individual pixels.

# Left arrow side
sense.set_pixel(3, 0, b)
sense.set_pixel(2, 1, b)
sense.set_pixel(1, 2, b)
sense.set_pixel(0, 3, b)
sense.set_pixel(2, 0, b)
sense.set_pixel(1, 1, b)

# Right arrow side
sense.set_pixel(4, 1, b)
sense.set_pixel(5, 2, b)
sense.set_pixel(6, 3, b)
sense.set_pixel(4, 0, b)
sense.set_pixel(5, 1, b)
for i in range(1, 8):
    sense.set_pixel(3, i, y)

sense.clear()
time.sleep(1)

# Perhaps an easier way to draw an arrow: use the set_pixels() method.
design = [
    w, w, b, b, b, w, w, w,
    w, b, b, y, b, b, w, w,
    w, b, w, y, w, b, w, w,
    b, w, w, y, w, w, b, w,
    w, w, w, y, w, w, w, w,
    w, w, w, y, w, w, w, w,
    w, w, w, y, w, w, w, w,
    w, w, w, y, w, w, w, w
    ]

sense.set_pixels(design)

# What about a downward-pointing arrow?
time.sleep(2)
sense.flip_v()

time.sleep(2)
# flip back up again
sense.flip_v()

# And a right-pointing arrow?
sense.set_rotation(90)

#---------------------------------------------------------
# Temperature, Pressure, and Humidity

while True:
    t = sense.get_temperature()
    # round to 1 decimal place
    t = round(t, 1)

    p = sense.get_pressure()
    # round to 1 decimal place
    p = round(p, 1)

    h = sense.get_humidity()
    # round to 1 decimal place
    h = round(h, 1)

    if t < 25:
        bg = b
    else:
        bg = r
    sense.show_message("Temp: {}; Press: {}; Hum: {}".format(t, p, h), back_colour=bg)





#!/usr/bin/env python

###
# Nathaniel Watson
# 2018-07-02
# De Anza College Academy
###


"""
Bakes a cake.
"""

import time

# The number of seconds to pause in each function.
DELAY = 2

def put_in_oven(minutes):
    """
    Args:
        minutes: `int`. How long to bake.
    """
    t = type(minutes)
    assert t == int, "minutes must be an integer, not a {}.".format(t)
    print("Baking for {} minutes.".format(minutes))
    time.sleep(DELAY)


def preheat_oven(temperature):
    """
    Args:
        temperature: `int`. The oven temperature, in Fahrenheit.

    """
    t = type(temperature)
    assert t == int, "temperature must be an integer, not a {}.".format(t)
    print("Preheating oven to {} Fahrenheit.".format(temperature))
    time.sleep(DELAY)

def butter_the_pans():
    print("Buttering the pans.")
    time.sleep(DELAY)

def add_flour(cups):
    """
    Args:
        cups: `float`. The number of cups of flour, i.e. 2.5.
    """
    t = type(cups)
    assert t == float, "cups must be a float, not a {}.".format(t)
    print("Pouring {} cups of flour.".format(cups))
    time.sleep(DELAY)

def add_frosting(flavor):
    """
    Args:
        flavor: `str`. The flavor of the frosting, i.e. chocolate, strawberry,
          vanilla.
    """
    t = type(flavor)
    assert t == str, "flavor must be a string, not a {}.".format(t)
    print("Spreading {} frosting, yum!!".format(flavor))
    time.sleep(DELAY)

def remove_from_oven():
    print("Getting the cake out of the oven.")
    time.sleep(DELAY)

def mix_batter():
    print("Mixing batter.")
    time.sleep(DELAY)

def bake_a_cake(type_of_cake):
    t = type(type_of_cake)
    assert t == str, "type_of_cake must be a string, not a {}.".format(t)
    print("Baking you a {} cake!".format(type_of_cake))
    # Call the above methods in the correct order to bake the cake.


bake_a_cake("German chocolate")

# INSTRUCTIONS:
#
# 1) Fill in the rest of the code for the function bake_a_cake() by calling the other functions
#    that are defined in this module.
#
# 2) In IDLE, use for loop to bake 5 cakes in a row.
#
# 3) In IDLE, use a while loop to bake an unlimited number of cakes.
#    Once you get this infinite while loop running, you can quite it
#    at any time by typing control-c. 


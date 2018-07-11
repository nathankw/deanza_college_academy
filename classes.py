#!/usr/bin/env python3                                                          
# -*- coding: utf-8 -*-                                                         


###                                                                             
# DeAnza College Academy
# Nathaniel Watson                                                              
# 2018-07-11
###


"""
Classes model things in the real world (or virtual things).

Lets demonstrate the use of classes by modeling a dog.
Dogs can do a lot of things, but we'll keep it simple and just make a
class that creates dogs that can bark and wag their tails.

Think of a class as a factory for making objects of whatever it is that
you are modeling. In our case, we are making dogs, and each dog will have a name.

Objects that you create from a class are formally called instances.
Functions defined in a class are formally called methods. 

You'll notice that I use the argument self in all of the methods below. That's
because self represents your dog instance when creating a new dog, or when calling methods on
an existing dog - don't omit it!
"""

class Dog():
    def __init__(self, name):
        # Every dog has a name that we specify when creating a new dog instance.
        # You can add more attributes in this __init__ methed as needed.
        self.name = name
        
    def bark(self):
        print("Barking!")
        
    def wag(self):
        print("Wagging tail")

    def play(self, minutes):
        print("{} is going out to play for {} minutes!".format(self.name, minutes))
        

lab = Dog("Labby")
lab.bark()
lab.wag()
lab.play(15)

print("See you later " + lab.name + ".")
print() 
collie = Dog("Lassie")
collie.bark()
collie.wag()
collie.play(30)
print("Until next time, " + collie.name + ".")

#!/usr/bin/env python3                                                                                 
# -*- coding: utf-8 -*-                                                                                
                                                                                                       
                                                                                                       
###                                                                                                    
# DeAnza College Academy                                                                               
# Nathaniel Watson                                                                                     
# 2018-07-11                                                                                           
### 


"""
This exercise teaches about scoping. When coding, you should keep in mind what "scope" a variable, 
function, class, etc, belongs to.

There is the global scope, and there are local scopes.

The global scope is the top-level part of your code (where there is no indentation). Anything
defined in the global scope is accessible everywhere in your program. 

A local scope is not visible to the entire program. For example, when you define a function, the 
contents of the function are in a local scope.  Try the exercises below to get a better 
understanding.
"""

x = 1 # x is defined in the global scope, and this thus visible everywhere. 
      # We call this x a global variable. 
def test():
    """
    Variables defined in functions are normally only visible from within the function and nowhere else. 
    """
    x = 3 # Anther variable named x. It's completly different from the global x. 
          # We call this x a local variable. 
    y = 10 # Another local variable.
    print(x) # prints 3

test() 

# I commented out the line of code below since it poduces NameError because y is not in the global scope.
#print(y)


def test2():
    print(x) # prints 1, becuase there is a variable named x in the global scope, and things
             # defined in the global scope are visible from anywhere. There isn't an x defined
             # here in the local scope of the function.

test2()

def change_global_x():
    """
    This example shows you can change a variable in the global scope. 
    """
    global x # Means use the x in the global scope, and don't make a local variable named x here. 
    x = 3    # Changes the value of x in the global scope

change_global_x()
print(x) # prints 3.  The global x has been modified by the function change_global_x.

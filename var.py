#!/usr/bin/env python
# Tim Layton
# dev@cybercoder.org
#
# Program: var.py  - episode 3
# Purpose: Introduce variables, local and global type
# Copyright 2014 Tim Layton <dev@cybercoder.org>
# Source: https://github.com/cybercoderdev/Learning-Python

# Note ------------------------------------------------------------------
# Tip - Python Docs
# Functions at https://docs.python.org/2.7/library/functions.html
# Tip - Python Std Types & Comparisons
# Comparisons at https://docs.python.org/2/library/stdtypes.html
# End -------------------------------------------------------------------

# Tip: Python is object oriented and not statically typed.  In other words
#      you don't need to declare the type because everything is an object.

i = 0 #declare var i and initialize with the integer zero
print i #print the value of i

# note: the first time run with the global commented out, then uncomment
# review the outputs and ensure you understand the difference between 
# local and global variables.

def myFunction(): #declare my own function 
  #global i #leave this commented out for first time
  i = "indigo" #declare i and initialize the local var with the string indigo
  # note: strings can be defined with single ' or double " quotes
  # tip: double quotes makes it easy to include apostrophes without terminating the string
  print i #print the current value of i
  
myFunction() #call the function
print i #print the value of i - with global commented out var i is local to function.

# note: uncomment the next two lines and then fix the error
# del i #delete the value of i
# print i #this will throw an error because var not initialized



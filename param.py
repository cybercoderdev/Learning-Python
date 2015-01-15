#!/usr/bin/env python
# Tim Layton
# dev@cybercoder.org
#
# Program: param.py  - episode 5
# Purpose: Pass parameters via the command line
# Copyright 2014 Tim Layton <dev@cybercoder.org>
# Source: https://github.com/cybercoderdev/Learning-Python
# Usage: python param.py one, two, three
# Note ------------------------------------------------------------------
# Tip - Python Docs
# Functions at https://docs.python.org/2.7/library/functions.html
# Tip - Python Std Types & Comparisons
# Comparisons at https://docs.python.org/2/library/stdtypes.html
# Tip argv info ----------------------------------------------------------
# see section 28.1 in Python Docs
# go to https://docs.python.org/2/library/sys.html?highlight=argv#sys.argv
# End -------------------------------------------------------------------

from sys import argv #only use what we need from sys module

# note argv holds variables that are passed via command line
# argv holds script name at argv[0]

scriptname, first, second, third = argv #unpacks argv to three variables

#print "The name of our script is:", scriptname
print "The first argument and variable is:", first
print "The second argument and variable is:", second
print "The third argument and variable is:", third
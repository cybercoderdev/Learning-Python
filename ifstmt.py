#!/usr/bin/env python
# Tim Layton
# dev@cybercoder.org
#
# Program: ifstmt.py  - episode 2
# Purpose: introduce the if/elif/else statement
# Copyright 2014 Tim Layton <dev@cybercoder.org>
# Source: https://github.com/cybercoderdev/Learning-Python

# Note ------------------------------------------------------------------
# There can be zero or more elif parts, and the else part is optional. 
# The keyword elif is short for else if, and is useful to avoid 
# excessive indentation. An if ... elif ... elif ... sequence is a 
# substitute for the switch or case statements found in other languages.
# Tip - Python Docs
# Functions at https://docs.python.org/2.7/library/functions.html
# Tip - Python Std Types & Comparisons
# Comparisons at https://docs.python.org/2/library/stdtypes.html
# End --------------------------------------------------------------------

print "Enter 1 if you like cats and 2 if you like dogs"

choice = raw_input("> ")

if choice == "1":
	print "Cats are loved by many, but I am allergic to them!"	
elif choice == "2":
	print "I love dogs too!"
else:
	print "You didn't enter a 1 for cats or 2 for dogs silly..."

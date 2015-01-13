#!/usr/bin/env python
# Tim Layton
# dev@cybercoder.org
#
# Program: fmt.py  - episode 4
# Purpose: Review the %d, %s, %r format specifiers
# Copyright 2014 Tim Layton <dev@cybercoder.org>
# Source: https://github.com/cybercoderdev/Learning-Python

# Note ------------------------------------------------------------------
# Tip - Python Docs
# Functions at https://docs.python.org/2.7/library/functions.html
# Tip - Python Std Types & Comparisons
# Comparisons at https://docs.python.org/2/library/stdtypes.html
# Tip - Docs - Built in Types
# https://docs.python.org/2/library/stdtypes.html
# Go to section 5.6.2 String Format Operations
# ----- common conversion types -----------------------------------------
# d - signed integer decimal
# i - signed integer decimal
# r - string (converts any python obj using repr())
# s - string (concerts any python obj using str())
# f - floating point decimal format
# c - single character (accepts int or single char)
# End -------------------------------------------------------------------

name = "Tim"
favos = "Linux"
favcomp = "MacBook Air"
mbaweight = 1 # 1 pound

print "%s's favorite OS is %s running on a %s that weighs about %d pounds" % (name, favos, favcomp, mbaweight)


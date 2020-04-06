# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 20:01:24 2019

@author: BHASKAR NEOGI
"""

print (abs.__doc__)
print (int.__doc__)
print (input().__doc__)

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num ** 2

print (square(2))
print (square.__doc__)
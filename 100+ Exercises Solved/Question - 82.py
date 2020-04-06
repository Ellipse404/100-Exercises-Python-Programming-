# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 00:18:03 2019

@author: BHASKAR NEOGI
"""
                 # Level-? *
#                     Unsuccessfull
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))

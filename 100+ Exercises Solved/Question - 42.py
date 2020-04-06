# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 18:58:25 2019

@author: BHASKAR NEOGI
"""

p = input("Enter The Elements of Tuple :  ").split(',')
k = []
for i in p :
    
    i = int(i)
    k.append(i)
    
k = tuple(k)
x = (len(k)//2)
print (k[:x])
print (k[x:])


# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:33:43 2019

@author: BHASKAR NEOGI
"""
                 # Level-? *

p = input("Enter : ").split(',')
li = []
for y in p :    
    li.append(int(y))
    
print("Your List : ",li)    
li = [x for (i,x) in enumerate(li) if i%2!=0]
print ("The Elements In Even Position : ",li)

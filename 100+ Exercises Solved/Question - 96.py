# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:01:39 2019

@author: BHASKAR NEOGI
"""
                 # Level-? **
                 
d = {}
p = input("Enter Your Words/Numbers/Syntax/Mixed : ")
for i in p :
    
    d[i] = d.get(i,0)+1
    
print ('\n'.join(['%s Has %s Times' % (x, y) for x, y in d.items()]))


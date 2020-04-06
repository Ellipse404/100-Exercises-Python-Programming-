# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:28:16 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2

import math as m
c = 50
h = 30
d = input("Enter The Comma ',' Seperated Numbers : ").split(",")
print("Here We Go With Your Number List",d)
print('''
      ''')
r = []                          # for listing the round values.
e = []                          # for listing the exact values.
for i in d :
    
    i = float(i)
    w = m.sqrt((2*c*i)/h)
    print("Exact Square Root of ",i,"is : ",w," ; Round At : ",round(w))
    e.append(str(w))
    r.append(str(round(w)))     # U may not Typecast it to string. 
    
print('''
''',"List of Exact Values : ",e,'''
      ''')
print(" List of Round Values : ",r)


        
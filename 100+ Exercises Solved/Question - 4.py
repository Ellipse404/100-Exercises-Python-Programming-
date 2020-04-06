# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:47:56 2019

@author: BHASKAR NEOGI
"""
          #    Level 1

try :
    l = input("Enter Comma(,) Seperated Numbers : ")
    y = l.split(",")
    t = tuple(y)
    print(t,y)
#    print(y)
       
    print("::------------  Another One  ------------::")
    
    k = input("Numbers : ")
    h = k.split(",")
    print(h)
    print(int(k))
    print(tuple(k))
except ValueError :
    print("Please Choose The Correct Value :")
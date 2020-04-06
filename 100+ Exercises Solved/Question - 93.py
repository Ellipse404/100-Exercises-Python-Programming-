# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:04:11 2019

@author: BHASKAR NEOGI
"""
                 # Level-? *

try :
    
    def Coffee(p) :
        
        k = input("Enter The Elements Of List Seperated by Comma(,) : ").split(',')
        v =[]
        for i in k :
            v.append(float(i))    
        print("List",p," : ",v)
        return v
            
    x = set(Coffee(1))
    w = set(Coffee(2))
    print(" Commom Elements In Sorted Order : ",sorted(list(x & w)))

except :
    print("Follow The Rules And Take Care While Typing !! ")
    pass
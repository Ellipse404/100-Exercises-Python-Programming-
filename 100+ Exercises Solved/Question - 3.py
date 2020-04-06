# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:27:10 2019

@author: BHASKAR NEOGI
"""
          #    Level 1

try :   
      
    x = int(input("Enter The Number :"))
    d = dict()
    for i in range(1,x+1) :
        
        d[i]=i*i
    print(d)
except ValueError :
    
    print("Here You Should Use Only Integer Values ")
    
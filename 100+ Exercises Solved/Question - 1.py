# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 18:11:28 2019

@author: BHASKAR NEOGI
"""
              #    Level 1
              
a = []
for i in range(2000,3201) :
    
    if(i%7==0 and i%5!=0) :
        
        a.append(str(i))
print(a)
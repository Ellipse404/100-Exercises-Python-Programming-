# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 19:34:35 2019

@author: BHASKAR NEOGI
"""

#def printDict():
    
d=dict()
for i in range(1,21):
    d[i]=i**2
for k in d.keys():	
    print (k,end=" ")
print("---------------------== : Squares : ==-----------------------")        		
for (x,j) in d.items():        
    print (j,end=" ")		

#printDict()
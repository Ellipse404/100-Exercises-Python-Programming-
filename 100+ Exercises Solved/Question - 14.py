# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:18:13 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2   

raw = input("Enter As You Wish : ")
k = {"U.C.":0,"L.C.":0}
for i in raw :
    
    if i.isupper() :
        k["U.C."] +=1
    elif i.islower() :
        k["L.C."] +=1
    else :
        pass

print('''================================
      
''',"UPPER CASE : ",k["U.C."],'''
''',"LOWER CASE : ",k["L.C."])

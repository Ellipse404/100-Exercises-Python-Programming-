# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 18:31:40 2019

@author: BHASKAR NEOGI
"""
           #   Level 1

try :
       
    def fact(x):
        
        if x == 0:
            return 1
        return x * fact(x - 1)    
    l = input("Enter Comma(,) Seperated Numbers : ")
    y = l.split(",")
    print("Here We Go With Your Number List : ",y)
    for i in y :
         
        print("Factorial of ",i,"is : ",fact(int(i)))

except ValueError :
        print("Invalid Value : Please Follow The Instructions ... !! ")
        
print("-------------------------------------------------------")


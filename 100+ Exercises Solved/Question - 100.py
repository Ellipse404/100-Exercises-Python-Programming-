# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:15:18 2019

@author: BHASKAR NEOGI
"""
                 # Level-? *
                 
print(" >>  In a Farm There Are Hens & Rabbits Only .😊...")
try :
    
    def solve(x,y):
        
    #    ns='No solutions!'
        for i in range(x+1):
            
            j=x-i
            if 2*i+4*j==y:
                return i,j
    #    return ns,ns
    heads=int(input("Enter The Number of Heads : "))
    legs=int(input("Enter The Number Of Legs : "))
    so=solve(heads,legs)                        # Unpacking Features : 
    print (" The Number of Hen in Farm : ",so[0],'''
    ''',"The Number of Rabbits in Farm : ",so[1])

except TypeError :
    print("Invalid Request ! Please Check Your Count !!")
except ValueError :
    print("Invalid Request ; We Can't Process It !!")
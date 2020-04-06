# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:54:45 2019

@author: BHASKAR NEOGI
"""
              # Level - 1
              
class String(object) :
    
    def __init__ (self) :                    # U may not use these 2 lines.
        self.s = ""    
        
    def getString(self) :             # If u take variables without self -> due to unused this value it'll show error.
        self.s = input("Enter The Value To Convert into String : ")         

# self without '.s' works as a normal variable & to execute self argument '.s' is used.
        
    def printString(self) :
        print("Output : ",self.s.upper())
        
k = String()
k.getString()
k.printString()
        
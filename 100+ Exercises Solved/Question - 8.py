# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:04:41 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2    

w = input("Enter the Words You Want To list Alphabetically Seperated By Comma ','  :: ").split(",")
w.sort()
print("Output In List : ",w)
print("Output In Comma Seperated Style : ",','.join(w))
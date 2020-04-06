# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:34:08 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2 *   

p = [i for i in input("Enter Numbers : ").split(",") if int(i)%2!=0]
print(",".join(p)," < || > ",list(p)," < || > ",tuple(p))
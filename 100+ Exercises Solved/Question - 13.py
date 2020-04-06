# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:51:28 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2 *   

raw = input("Enter As You Wish : ")
d={"DIGITS":0, "LETTERS":0, "OTHERS":0}
for i in raw:
    
    if i.isdigit() :        
        d["DIGITS"] += 1
    elif i.isalpha() :        
        d["LETTERS"] +=1
    else :        
        d["OTHERS"] += 1
        pass
    
print ('''::-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_::

''',"LETTERS :", d["LETTERS"],'''
''',"DIGITS :", d["DIGITS"],'''
''',"SPACE & OTHERS :", d["OTHERS"])



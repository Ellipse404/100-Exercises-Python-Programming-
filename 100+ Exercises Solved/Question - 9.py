# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:21:23 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2    *

lines = []
print("Enter Your Lines & Presss Enter Twice To Get Output : ")
while True:              # This while loop'll take care of multiline input.
    
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break
print('''Output :
    ''')
for sentence in lines:
    
    print(sentence)

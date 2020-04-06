# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:28:45 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2    **

inp = input("Enter The Row & Column Number Seperated by Comma ','  : ")
dimensions= [ int(i) for i in inp.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    
    for col in range(colNum):
        
        multilist[row][col]= row*col

print (multilist)
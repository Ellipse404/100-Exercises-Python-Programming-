# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:03:37 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2    

binary = input("Enter The Binary Numbers : ").split(',')
a = []
for i in binary :
    decimal = int(i,2)
    print("Decimal of ",i,"is : ",decimal)
    if not decimal%5 :     # This line is as same as " if decimal%5==0 : ".
        a.append(i)
print('''
''',"The List of Binary,Divisible By 5 is : ",','.join(a))
        



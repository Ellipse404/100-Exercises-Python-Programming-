# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:01:22 2019

@author: BHASKAR NEOGI
"""
                 # Level - 3 *

from operator import itemgetter as it
p = []
print("Follow The Format : Name,Age,Height ; Make Each Option With Same Number of Values(ex : 03 for 3) :")
while True :
    
    s = input()
    if not s :
        break
    
    p.append(tuple(s.split(",")))
print ("Sorted In Order Name,Age,Height : ",'''
''',sorted(p,key = it(0,1,2)))

print('''
''',">->->->  Sorted By Name  <-<-<-< : ",'''
''',sorted(p,key = it(0)),'''
''',">->->->  Sorted By Age  <-<-<-< : ",'''
''',sorted(p,key = it(1)),'''
''',">->->->  Sorted By Height  <-<-<-< :",'''
''',sorted(p,key = it(2)))
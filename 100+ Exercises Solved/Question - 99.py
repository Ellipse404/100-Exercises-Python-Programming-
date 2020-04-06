# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:17:23 2019

@author: BHASKAR NEOGI
"""
                 # Level-? *

import itertools as it
try :

    k = int(input("Press 1 for Automatic  & 0 for Manually Choose Numbers to Permutate : "))
    if k==1 :
        print(list(it.permutations([int(i) for i in range(int(input("Enter The Range: ")))])))
    elif k==0 :
        
        p = input("Enter The Numbers Seperated By Comma (,): ").split(',')
        v = []
        for i in p :
            
            v.append(int(i))
        print(list(it.permutations(v)))
        
    else :
        print("Please Follow The Instruction Carefully !! ")

except ValueError :
    print("Please Press The Correct Key Words According to Instruction !! ")



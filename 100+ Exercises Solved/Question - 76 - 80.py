# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 00:29:31 2019

@author: BHASKAR NEOGI
"""
                 # Level-? *

import random
# Type : 1
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 6))
# Type : 2
print(random.sample(list(i for i in range(1,1001) if i%5==0 and i%7==0), 6))


print ("5 Random Numbers Under 100 : ",random.sample(range(100), 5))
print (random.choice([i for i in range(201) if i%5==0 and i%7==0]))
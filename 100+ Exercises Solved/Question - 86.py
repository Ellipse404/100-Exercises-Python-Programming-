# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:03:40 2019

@author: BHASKAR NEOGI
"""
                 # Level-? *

subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    
    for j in range(len(verbs)):
        
        for k in range(len(objects)):
            
            sentence = ("%s %s %s." % (subjects[i], verbs[j], objects[k]))
            print (sentence)

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 19:55:30 2019

@author: BHASKAR NEOGI
"""

class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

j = Person("Jerry")
print ("%s name is %s" % (Person.name, j.name))

n = Person()
n.name = "Tom"
print ("%s name is %s" % (Person.name, n.name))
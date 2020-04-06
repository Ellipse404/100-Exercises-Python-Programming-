# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:26:56 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2   

print("<_<  Printing In 'a+aa+aaa+aaaa' Format; where a Is Your Input  >_>")
p = input("Enter The Value : ")
p1 = int("%s" % p)
p2 = int("%s%s" % (p,p))
p3 = int("%s%s%s" % (p,p,p))
p4 = int("%s%s%s%s" % (p,p,p,p))

print(p1+p2+p3+p4)


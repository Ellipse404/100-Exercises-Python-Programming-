# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:16:25 2019

@author: BHASKAR NEOGI
"""
                 # Level-? *

import re
email = input("Enter Your Email Address : ").lower()
# id name : 

p1 = "(\w+)@((\w+\.)+(com))"
r1 = re.match(p1,email)
print ("Your Id Name : ",r1.group(1))
# company name : 

p2 = "(\w+)@(\w+)\.(com)"          # IF U DO AS SAME AS P1 THEN '.COM' WILL ADD WITH COMPANY NAME.
r2 = re.match(p2,email)
print ("Your Mail Company Name : ",r2.group(2))
# domain name : 

p3 = "(\w+)@(\w+)(.\w+)"
r3 = re.match(p3,email)
print("Your Domain Name : ",r3.group(3))



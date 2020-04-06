# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:53:08 2019

@author: BHASKAR NEOGI
"""
                 # Level - 3 *


import re
print("     :: <>  Welcome To Our PYTHONIC  PASSWORD MAKER  <> :: ",'''

''',
"==============================================================")

pwd = []
print("Choose  Your  Own  Password . create some sample password seperated by comma ")
p = input("ENTER YOUR PASSWORD : ").split(",")
for i in p :
    
    if(len(i)<6 or len(i)>12) :
        continue        
    else :
        pass
    
    if not re.search("[a-z]",i) :
        continue
    elif not re.search("[A-Z]",i) :
        continue
    elif not re.search("[0-9]",i) :
        continue
    elif not re.search("[$#@%*&!^]",i) :
        continue
    elif re.search("\s",i) :
        continue
    else :
        pass
    
    pwd.append(i)
print(",".join(pwd))

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:51:15 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2 

print("    _/\_/\_ :: <>  Welcome To Our PYTHONIC BANK  <> :: _/\_/\_",'''

''',
"==============================================================")

while(True) :
    
    print("How Can We Help You !",'''
      '''," 1 : Deposit",'''
      '''," 2 : Withdraw",'''
      '''," 3 : Update",'''
      '''," 4 : Exit Process")
    p = int(input ("Enter Your Choice : "))
    
    if(p==1) :
        na = 0
        d = int(input("Enter The Amount : "))
        na += d
    elif(p==2) :
        w = int(input("Enter The Amount : "))
        na -= w
    elif(p==3) :
        print(''' _______________________________________
   ''',"Your Current Balance Is : ",na,'''
''',"_______________________________________")
    elif(p==4) :
        break
    else :        
        print("Process Gone Wrong !!")
        

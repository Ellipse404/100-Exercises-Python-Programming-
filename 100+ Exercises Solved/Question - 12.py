# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 22:05:03 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2    

values = []
x = int(input("Enter The Starting range : "))
y = int(input("Enter The Ending range : "))
for i in range(x, y+1):
    
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        
        values.append(s)
print( ",".join(values))
               
# Unsuccessfull ->-> ** 

#v = []
#m = input()
#p = ",".join(m)
#k = len(m)
#for i in m :
#    i = int(i)
#    
#    if (i%2!=0) :
#        continue    
#    else :
#        v.append(i)
#print(v)
                 
#values = []
#x = int(input("enter The value of starting range : "))
#y = int(input("enter The value of ending range : "))
#for i in range(x, y+1):
#    i = str(i)
#    v = []
#    m = i.split(",")
##    k = len(m)
#    for j in m :
#        j = int(j)
#        if (j%2==0) :
#            v.append(j)
##            print(v)
#            v = str(v)
#            print(v)
#            continue
        
#        elif(j%2!=0) :
#            v.append(j)
##            print(v)
#            v = str(v)
#            print(v)
                 

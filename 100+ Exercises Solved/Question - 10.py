# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:50:45 2019

@author: BHASKAR NEOGI
"""
                 # Level - 2    

p = input("Enter Your Words Seperated By a WhiteSpace To Sort : ")
words = [words for words in p.split(" ")]
print(" Different Type of Sorted List :")
print("I :"," ".join(sorted(set(words))))   # set function use a word once only.
print("II :",sorted(words))                 # so, in case of 2s['and's,'hello's,'world's] printed only once.
print("III :",",".join(sorted(words)))
print("IV :",tuple(sorted(words)))




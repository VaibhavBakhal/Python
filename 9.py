# -*- coding: utf-8 -*-
"""
Python program to print even length words in a string
Input: s = "This is a python language"
Output: This is python language
"""
s = "This is a python language"
l=s.split()
result=""
for i in l:
    count=0
    for j in i:
        count+=1
    if count%2==0:
        result=result+i+" "
print(result)
        
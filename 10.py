# -*- coding: utf-8 -*-
"""
Python program to capitalize the first and last character of each word in a string
Given the string, the task is to capitalise the first and last character of each word in a string. Examples:

Input: hello world 
Output: HellO WorlD
"""
Input="hello world"

l=Input.split()
for i in l:
    c=""
    for j in range(len(i)):
        if j ==len(i)-1 or j==0:    
            c=c+(i[j].upper())
        else:
            c=c+i[j]
    print(c+" ",end="")


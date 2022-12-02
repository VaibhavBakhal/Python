# -*- coding: utf-8 -*-
"""
Python program to find the sum of a Sublist
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
result is [11,15,22]
"""
list =[[4, 1, 6], [7, 8], [4, 10, 8]]
l=[]
for i in list:
    c=sum(i)
    l.append(c)
print(l)
    
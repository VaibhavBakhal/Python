# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 19:27:12 2022

@author: vaibh
"""

a=[0, 1, 2, 3, 4, 5]

sum=0

b=int(input("enter value of i"))
if b==len(a) or b<len(a):
    for j in range(b):
        sum+=a[j]
    if sum==b:
        print('True')
    else:
        print('False')
else:
    print('Run code again and put the value in range')

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 07:36:12 2022

@author: vaibh
"""

a=[19, 19, 15, 5, 5, 5, 2]
b= a[4]
count=0
for i in a:
    if i==b:
        count+=1
if count==3 and len(a)==8:
    print('True')
else:
    print('False')
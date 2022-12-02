# -*- coding: utf-8 -*-
"""
2. Write a program to read a list of n integers (positive

as well as negative). Create two new lists, one
having all positive numbers and the other having
all negative numbers from the given list. Print all
three lists.
"""
lst=[1,2,3,2,1,-1,-6,-7,1,5,6,-7,-4,5,-6,-5,9]
p=[]
n=[]
for i in lst:
    if i>0:
        p.append(i)
    else:
        n.append(i)
print(p,n)
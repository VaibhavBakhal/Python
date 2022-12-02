# -*- coding: utf-8 -*-
"""
4. Write a function to return the second largest number
from a list of numbers.
"""
lst=[1,2,3,5,2,4,5,6,3,4,4,6,3,6,8,2,2,3,1]
lst.sort()
print(lst)
m=0
sl=[]
for i in lst:
    if i not in sl:
        sl.append(i)
for i in sl:
    count=0
    for j in lst:
        if j==i:
            count+=1
    if count>m:
        m=count
print(lst[len(lst)-m:len(lst)-m+1])
    

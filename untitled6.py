# -*- coding: utf-8 -*-
"""
5. Write a program to read a list of n integers and find
their median.
Note: The median value of a list of values is the
middle one when they are arranged in order. If there
are two middle values then take their average.
Hint: You can use an built-in function to sort the list
"""
lst=[1,2,3,2,2,5,6,7,8,9,1,4]
lst.sort()
print(lst)
m=0
if len(lst)%2==0:
    c,d=lst[(len(lst)//2)-1], lst[(len(lst)//2)]
    m=(c+d)/2
    
else:
    m=lst[(len(lst))//2]
print(m)
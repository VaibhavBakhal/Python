# -*- coding: utf-8 -*-
"""
Python Program to Square Each Odd Number in a List using 
List Comprehension data=[1,2,3,4,5,6,7]
[1, 9, 25, 49]   
"""
data=[1,2,3,4,5,6,7]
l=list(i*i for i in data[0::2])
print(l)
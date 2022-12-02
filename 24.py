# -*- coding: utf-8 -*-
"""
Write a function that returns the largest element of
the list passed as parameter.
"""
def fun1(lst):
    lst.sort()
    return lst[len(lst)-1::]
lst=[1,2,4,3,5,3,6,2,6,6,2,6,2]
print(fun1(lst))
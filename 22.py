# -*- coding: utf-8 -*-
"""
1. Write a program to find the number of times an
element occurs in the list.

"""
def reocur(lst,j):
    count=0
    for i in lst:
        if i==j:
            count+=1
    return count

lst=input().split()
j=input()
print(reocur(lst, j))
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:44:54 2022

@author: vaibh
"""

st="this  is very   funny and cool.Indeed"
def fun1(st):
    
    a=""
    for i in st:
        if i ==".":
            a=a+i+" "
        else:
                a=a+i
    lst=a.split()
    final=""
    for i in lst:
        final=final+i+" "
    print(final)
fun1(st)
# -*- coding: utf-8 -*-
"""
returns a list of  Odd Frequency Characters
string="welcometoknowit"
odd frequency char :[ 'l', 'c', 'o', 'm', 'k', 'n', 'i']
"""
s="welcometoknowit"
c=""
lst=[]
for i in s:
    if i not in c:
        c=c+i
for i in c:
    count=0
    for j in s:
        if i==j:
           count+=1
    if count%2==1:
        lst.append(i)
print(lst)
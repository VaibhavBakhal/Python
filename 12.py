# -*- coding: utf-8 -*-
"""
returns a list of Least Frequent Character in String
string="welcometoknowit"
least frequency char :['l','c','m', 'k', 'n', 'i']
"""
g="welcometoknowit"
v=""
l=[]
for i in g:
    if i not in v:
        v=v+i
for i in v:
    count=0
    for j in g:
        if i==j:
            count+=1
    if count==1:
        l.append(i)
print(l)
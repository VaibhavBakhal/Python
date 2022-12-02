# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:52:42 2022

@author: vaibh
"""

#l=[222,3,35,62,124,61,29,375,66,7]
l=[2,3,5,22,24,7,24]
#out=[222,2,62,124,3,66,7]
count=0
o=[]

for i in range(len(l)):
    if l[i]%2!=0 and l[i]>0:
        count+=1
        continue
    if count>=2:
        o.append(count)
        count=0
    if count==1:
        o.append(l[i-1])
        count=0
    if l[i]%2==0:
        o.append(l[i])
d=[]
if count==1:
    d=l[len(l)-1::]
for i in d:
    o.append(i)

print(o)
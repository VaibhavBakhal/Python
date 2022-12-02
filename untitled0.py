# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 06:57:47 2022

@author: vaibhav Bakhal
"""

s='aaaabbbccccd'
count=0
str1=s[0]
c=''
for i in s:
    if i==str1:
        count+=1
    else:
        c=c+str(count)+str1
        str1=i
        count=1
c=c+str(count)+str1
print(c)
        
        
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 08:28:13 2022

@author: vaibh
"""

c=1
d=1
e=0
print(c,"\n",d)
for i in range(10):
    e=c+d
    c=e
    d=d
    print(e)
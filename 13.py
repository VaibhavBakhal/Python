# -*- coding: utf-8 -*-
"""
returns a list of Maximum  Frequent Character in String
string="welcometoknowit"
max frequency char :['o']
"""
g="welcometoknowit"
s=""
m=0
v=""
for i in g:
    count=0
  
    
    for j in g:
        if j==i:
            count+=1
    if count>m:
        m=count
        v=v+i
        
        
print(v[len(v)-1::])
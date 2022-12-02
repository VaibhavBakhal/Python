# -*- coding: utf-8 -*-
"""
Program to print duplicates from a list of integers

Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]

Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
"""

list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
s=[]
output_list=[]
for i in list:
    if i not in s:
        s.append(i)
#s=[10, 20, 30, 40, 50, -20, 60]
for i in s:
    count=0

    for j in list:
        if j==i:
            count+=1
    if count>1:
        output_list.append(i)
print(output_list)
        

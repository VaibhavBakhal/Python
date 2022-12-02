# -*- coding: utf-8 -*-
"""
Reverse Row sort in Lists of List
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]
"""
l=[[4, 1, 6], [7, 8], [4, 10, 8]]
final=[]
for i in l:
    i.sort()
    print(i)
    i.reverse()
    #print(i)
    final.append(i)
print(final)

# -*- coding: utf-8 -*-
"""
Uncommon elements in Lists of List
The original list 1 : [[1, 2], [3, 4], [5, 6]]
The original list 2 : [[3, 4], [5, 7], [1, 2]]
The uncommon of two lists is : [[5, 6], [5, 7]]
"""
list1 =[[1, 2], [3, 4], [5, 6]]
list2= [[3, 4], [5, 7], [1, 2]]
uncommon=[]
for i in list1:
    if i not in list2:
        uncommon.append(i)
for i in list2:
    if i not in list1:
        uncommon.append(i)
print(uncommon)
        
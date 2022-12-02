# -*- coding: utf-8 -*-
"""

Sum of number digits in List
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]
"""
l=[12, 67, 98, 34]
x=[]
for i in range(len(l)):
    l[i]=str(l[i])

for i in l:
    c=0
    for j in i:
        j=int(j)
        #print(j)
        c+=j
    x.append(c)
print(x)














"""
a=[12,67,98,34]
for
a[i]=str(a[i])
a=['12','67','98','34']
l=[]
for l(ghumana he)
    sum=0
    for l(pahale element me ghum raha hu):
        i=int(i)
        sum+=i
    l(adding sum in list)
print(l)


"""










        
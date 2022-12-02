"""
Python Program to get Maximum product of elements of list in a 2D list
Input :  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output : 504
Explanation:1*2*3 = 6, 4*5*6 = 120, 7*8*9 = 504
Since maximum is 504.
"""
import numpy as np 
l=list(input().split())
for i in range(len(l)) :
    l[i]=int(l[i])
    
print(l)   
a=np.array(l).reshape(3,3)
print(a)
c=np.sum(a,axis=1)
print(c)
print(max(c))
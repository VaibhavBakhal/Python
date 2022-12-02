import numpy as np
l=[1,2,3,4]
l2=[2,3,4,4]
l2.d()
s={1,2,3,4,5}
s1={6,7,8,9,10}
s1.intersection(s)
#c=l[len(l)//2]
#d=l2[len(l2)//2]
set(l) & set(l2)
print(set(l) & set(l2))
l2=[]
a=np.array([[1,2,3],[4,5,6]])
l2=a.tolist()
l3=a.cumsum()
l4=a.cumprod()
l5=a.flatten().tolist()

print(a)
print(l2)
print(l3)
print(l4)
print(l5)

s="adkNKdnvfvfdb"
b=s.rpartition("d")
print(b)
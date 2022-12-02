"""l=["vaibhav", "shubham", "dfgbodfhere","rgrei","grege"]
m=0
lst=[]
for i in l:
    if len(i)>m:
        m=len(i)
        lst.append(i)
print(lst[len(lst)-1::])
"""
l=["vaibhav", "shubham", "dfgbodfhere","rgrei","grege"]      
n=7
def fun1(l,n):
    for i in l:
        if len(i)>n:
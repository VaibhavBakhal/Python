a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
b=input().split()
for i in range(len(b)):
    b[i]=int(b[i])    
list(product(a,b))
print(c)
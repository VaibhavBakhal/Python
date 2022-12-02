l=int(input("Enter a number"))
rev=0
while l!=0:
    rev= rev*10 +l%10
    l=l//10
print(rev)



l=int(input("Enter a number"))
n=l
s=0
while n!=0:
    s+=(n%10)**3
    n=n//10
if s==l:
    print("Amstring numberr")
else:
    print("not ")
    
#0,1,1,2,3,5,8
l= int(input("Enter a number"))
a=0
b=1
print(a)
for i in range(l+1):
    s=a+b
    a=b
    b=i
    
    print(s)
    

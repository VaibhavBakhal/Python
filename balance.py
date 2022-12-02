n=int(input("Number of Transaction"))
balance=0
lst=[]
for i in range(n):
    lst=input().split()
    lst[1]=int(lst[1])
    if lst[0]=='C' or lst[0]=='c':
        
        balance+=lst[1]
    else:
        balance-=lst[1]
    if balance<0:
        print("balance is zero kindy cridit")
        
print(balance)
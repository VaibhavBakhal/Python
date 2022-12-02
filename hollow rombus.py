l=[]
for j in range(1,3+1):
    for i in range (1,3-j+1):
        print(' ',end=" ")
    for i in range (1,2*j):
        if i==1 or i==2*j-1:
            print('c',end=" ")
        else:
            print(" ",end=" ")
    print()
#    a=(("(.)_(.)"*1).center(30," "))
#print(a)
for j in range(3-1,0,-1):
    for i in range (1,3-j+1):
        print(' ',end=" ") 
    for i in range (1,2*j):
        if i==1 or i==2*j-1:
            print('c',end=" ")
        else:
            print(" ",end=" ")
    print("")
    
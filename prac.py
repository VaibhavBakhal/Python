



l=['class01#aman#56#141#21','class01#rohan#55#151#11','class01#rajesh#26#140#31']
lst=[]
person=""
m=0
s=0
for i in l:
    lst=i.split("#")
    for j in range(2,len(lst)):
        lst[j]=int(lst[j])
    s=lst[2]+lst[3]+lst[4]
    if s>m:
        person=lst[1]
        m=s
        s=0
print(person,m)    
        
d={
   1:"abc",
   2:"efg",
   3:"hij",
   }
set(d[1])
print(d)
print(d.setdefault(1,"xyz"))# if key is allready there it return the value only
print(d.setdefault(5,"sonali"))#if key is not present it insert key and value
print(d)# here key 5 is not added so key and value is added 



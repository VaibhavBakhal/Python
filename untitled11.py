# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:59:26 2022

@author: vaibh
"""

d={
   "vai":"9854939593",
   "shu":"485930503",
   "arti":"8976435334"
   }
print(d)
d["arti"]="111111111"
print(d)
d["Ankita"]="22222"
print("Ankita added in last\n",d)
print(d["vai"])
c=input()
if c in d.keys():
    print(d["vai"])
else:
    print("none")
print(d.keys())
print(d.values())
str(d)
print(d)
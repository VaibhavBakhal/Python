# -*- coding: utf-8 -*-
"""
Given a String list, extract frequency of specific characters 
in the whole strings list.
Input : test_list = [“geeksforgeeks is best for geeks”], 
chr_list = [‘e’, ‘b’, ‘g’, ‘f’] 
Output : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 2} 
"""
test_list = "geeksforgeeks is best for geeks"
chr_list = ["e","b","g","f"]
lst=test_list.split()
d={}
for i in chr_list:
    count=0
    for j in test_list:
        if j ==i:
            count+=1
    d[i]=count
print(d)

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 07:43:05 2022

@author: vaibh
"""

a=['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsfrew']
#str1=a[len(a)]
if a[len(a)-2] in a[len(a)-1]:
    print('True')
else:
    print('False')
    
b=[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980]
count=0

for i in range(len(b)-1):
    c=int(b[i+1])
    d=int(b[i])
    if (c-d)==10:
        count+=1
if count==len(b)-1:
    print('True')
else:
    print('False')


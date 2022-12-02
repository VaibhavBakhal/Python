# -*- coding: utf-8 -*-
"""
The record of a student (Name, Roll No.,
Marks in five subjects and percentage of
marks) is stored in the following list:
stRecord = ['Raman','A-36',[56,98,99,72,69],
 78.8]
Write Python statements to retrieve the following
information from the list stRecord.
a) Percentage of the student
b) Marks in the fifth subject
c) Maximum marks of the student
d) Roll no. of the student
e) Change the name of the student from
 ‘Raman’ to ‘Raghav’
"""
stRecord = ['Raman','A-36',[56,98,99,72,69],78.8]
print("percentage",stRecord[3])
print("marks in 5th sub",stRecord[2][4])
print("max marks ",max(stRecord[2]))
print("Roll no",stRecord[1])
stRecord[0]="Raghav"
print(stRecord)
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:26:34 2024

@author: omenc
"""
"""
a
97
89
83
79
73
71
67
61
59
53
47
43
41
37
31
29
23
19
17
13
11
7
5
3
2

"""
#Prime Numbers!
j = 0
i = 0
print("This Program will give you the values from 2 to your choice that are prime")
myNumber = int(input("input a integer greater than 2\n"))
val = myNumber
print("\n\n\n\n")
for i in range(myNumber, 2, -1):
    #checks if prime
    for j in range(i - 1, 1, -1):
        #if not prime break
        if(i % j == 0):
            break
        #if gets to the end (2) and isnt prime from previous if statement, then print that val as one of the prime vals
        elif(j == 2):
            print(i)
#say 2 seperately because the check doesnt work on this
print("2")
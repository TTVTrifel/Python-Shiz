# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:26:50 2024

@author: omenc
"""
"""
a.
37 occurances of e

b.
16 occurances of i

c.
1 occurances of x

d.
3 occurances of ?




"""


count = 0
repeat = True
while(repeat == True):
    passage = input("Please Enter a Passage of 200 Characters or More Below:\n")
    while len(passage) < 200:
        print(len(passage))
        passage = input("Try Again, Enter a Passage of 200 Characters or More Below:\n")
    check = str(input("Letter to check for:"))
    while check.isalpha() == False or len(check) >= 1:
        if check.isnumeric() == False and len(check) <= 1:
            break
        check = input("Please Enter a Valid Letter:")
    count = passage.count(check)
    print(str(count) + " occurances of " + check)
        
    repeat = input("Continue? Enter YES or NO:")
    while repeat != "YES" and repeat != "NO":
        repeat = input("Please Try Again! Continue? Enter YES or NO:")
    if repeat == "YES":
        repeat = True
    if repeat == "NO":
        repeat = False




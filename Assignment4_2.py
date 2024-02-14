# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:41:06 2024

@author: omenc
"""
"""
a
37

b
16

c
1

d
3

"""



meh = True
cont = True
while(cont == True):
    i = 0
    occur = 0
    passage = str(input("input the passage of your choosing, must be 200 characters or more\n"))
    char = str(input("what character would you like to search for?\n"))
    if((len(passage)) > 200):
        while(i <= len(passage) -1):
            print(passage[i])
            i = i + 1
            if(str(passage[i - 1]) == char):
                occur = occur + 1
        print(len(passage))
        if(len(passage) < 200):
            break
        print(str(occur) + " occurances of " + char)
        yup = str(input("input \"stop\" to Stop and \"cont\" to Continue\n"))
        if(yup == "stop"):
            break
    else:
        print("please try again")
    



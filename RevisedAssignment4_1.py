# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 19:38:27 2024

@author: omenc
"""

"""
a.
12 is the solution

b.
9 is the solution
c.
4 is the solution
d.
1 is the solution

"""




int1 = 0
int2 = 0
Mode = ""
repeat = True

while repeat == True:
    Mode = input("enter Mode: ")
    while Mode != "GCF" and Mode != "LCM":
        Mode = input("please try again, choose either GCF or LCM: ")
    #Int1
    try:
        int1 = input("enter Integer 1:")
        int1 = int(int1)
    except:
        while type(int1) != int:
            try:
                int1 = int(int1)
            except:
                int1 = input("please try again, choose a valid integer: ")

    try:
        int2 = input("enter Integer 2:")
        int2 = int(int2)
    except:
        while type(int2) != int:
            try:
                int2 = int(int2)
            except:
                int2 = input("please try again, choose a valid integer: ")
    """         
    print(Mode)
    print(int1)
    print(int2)
    """

    if(Mode == "LCM"):
        sol1 = int1
        sol2 = int2
        while(sol1 != sol2):
            while(sol1 < sol2):
                sol1 += int1
            while(sol2 < sol1):
                sol2 += int2
        print(str(sol1) + " is the solution")

    if(Mode == "GCF"):
        solved = False
        if(int1 > int2):
            i = int2
            o = int1
            t = int2
        else:
            i = int1
            o = int2
            t = int1
        while(solved == False):
            if(o % i != 0):
                i = i - 1
                #print(i)
            else:
                if(t % i == 0):
                    break
                else:
                    i = i - 1
                    #print(i)
            
        print(str(i) + " is the solution")
    repeat = input("Continue? Enter YES or NO:")
    while repeat != "YES" and repeat != "NO":
        repeat = input("Please Try Again! Continue? Enter YES or NO:")
    if repeat == "YES":
        repeat = True
    if repeat == "NO":
        repeat = False

    
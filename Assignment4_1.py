# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:05:19 2024

@author: omenc
"""
"""
a
12

b
9

c
4

d
1

"""

i = 1
live = True
solved = False
while(live == True):
    choice = str(input("Choose either \"LCM\" or \"GCF\"\n"))

    if(choice == "LCM"):
        int1 = int(input("input an integer of your choice\n"))
        sol1 = int1
        int2 = int(input("input a second integer of your choice\n"))
        sol2 = int2
        
        while(sol1 != sol2):
            while(sol1 < sol2):
                sol1 += int1
                print(sol1)
            while(sol2 < sol1):
                sol2 += int2
                print(sol2)
        print(str(sol1) + "is the solution")

    if(choice == "GCF"):
        int1 = int(input("input an integer of your choice\n"))
        
        int2 = int(input("input a second integer of your choice\n"))

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
                print(i)
            else:
                if(t % i == 0):
                    break
                else:
                    i = i - 1
                    print(i)
        
        print(str(i) + " is the solution")
    
    check = str(input("\"Stop\" to End and \"cont\" to Continue\n"))
    if(check == "Stop"):
        live = False
        
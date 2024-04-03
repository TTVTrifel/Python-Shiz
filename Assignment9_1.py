# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:08:10 2024

@author: omenc
"""




"""
Create function that allows for 3 lists with 3 elements each, or 1 list with 9

check if the 9 values are not repetative, and if they are all ints

"""


def Sudoku(*Nums):
    Bers = []
    for i in Nums:
        for a in i:
            if(type(a) == list):
                for b in a:
                    Bers.append(b)
            else:
                Bers.append(a)
    #print(Bers)
    #print(len(Bers))
    for c in range(0,len(Bers)):
        #compare with the other ints
        Check = []
        Check = Bers[:c] + Bers[c + 1:]
        #print(Check)
        for d in range(0,8):
            #print(Bers[c])
            #print(Check[d])
            if(Bers[c] == Check[d]):
                return "Duplicate Values"
            if(type(Bers[c]) != int):
                return "Illegal Values"
    return "Valid"
print(Sudoku([1,2,3,4,5,6,7,8,9]))
print(Sudoku([[5, 3, 4], [6, 7, 2], [1, 9, 8]]))
print(Sudoku([[9, 9, 2], [3, 4, 8], [5, 6, 7]]))
print(Sudoku([[8, 5, 9], [4, 2, 6], [8, 1, 3]]))
print(Sudoku([[7, 6, 1], [6, 8, 5], [3, 9, 6]]))
print(Sudoku([[4, 2, "E"], [7, 9 , "I"], [8, "S", 6]]))
print(Sudoku([[6, 7, 8], [1, 9, 5, 3], [3, 4, 2]]))




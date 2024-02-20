# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:30:34 2024

@author: omenc
"""
"""
a

3

    [1]
  [1, 1]
[1, 2, 1]


b

5

        [1]
      [1, 1]
    [1, 2, 1]
  [1, 3, 3, 1]
[1, 4, 6, 4, 1]

c

7

            [1]
          [1, 1]
        [1, 2, 1]
      [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
  [1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]

d

10

                  [1]
                [1, 1]
              [1, 2, 1]
            [1, 3, 3, 1]
          [1, 4, 6, 4, 1]
        [1, 5, 10, 10, 5, 1]
      [1, 6, 15, 20, 15, 6, 1]
    [1, 7, 21, 35, 35, 21, 7, 1]
  [1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

"""

rows = int(input("how many rows\n"))
odd = False
prev= []
cur = []
calc = 0
spaces = 0
#cycle through rows, first is 0
for rowNum in range(1, rows + 1):
    #calc the required seats to be calculated for this row and if odd
    spaces = rows - rowNum
    calc = rowNum // 2
    if(calc < rowNum / 2):
        odd = True
        calc = calc + 1
    #calculate required seat vals
    for seatVal in range(1, calc + 1):
        if(seatVal == 1):
            cur.append(int(seatVal))
        else:
            cur.append(int(prev[seatVal -2] + prev[seatVal - 1]))
            
    if(odd == False):
        cur = cur + cur[::-1]
    else:
        cur = cur + (cur[::-1])[1:]
    print("  "*spaces + str(cur))
    #reset odd to False
    odd = False
    prev = cur.copy()
    cur.clear()
    



"""
Get number of rows requested
take the rowNum if greater than 1 and // it. if that is less than half add one
this tells us how much work to do










[This marks getting the ordering and repeating right]
rows = int(input("how many rows"))
odd = False
prev= ""
cur = ""
calc = 0
#cycle through rows, first is 0
for rowNum in range(1, rows + 1):
    #calc the required seats to be calculated for this row and if odd
    calc = rowNum // 2
    if(calc < rowNum / 2):
        odd = True
        calc = calc + 1
    #calculate required seat vals
    for seatVal in range(1, calc + 1):
        cur = cur + str(seatVal)
    if(odd == False):
        cur = cur + cur[::-1]
    else:
        cur = cur + (cur[::-1])[1:]
    print(cur)
    #reset odd to False
    odd = False
    prev = cur
    cur = ""
    


[Works a little, but because its a string, it reverse 10 into 01, and that messes up the math]
rows = int(input("how many rows"))
odd = False
prev= ""
cur = ""
calc = 0
#cycle through rows, first is 0
for rowNum in range(1, rows + 1):
    #calc the required seats to be calculated for this row and if odd
    calc = rowNum // 2
    if(calc < rowNum / 2):
        odd = True
        calc = calc + 1
    #calculate required seat vals
    for seatVal in range(1, calc + 1):
        if(seatVal == 1):
            cur = cur + "1"
        else:
            cur = cur + str(int(prev[seatVal - 2]) + int(prev[seatVal -1]))
    if(odd == False):
        cur = cur + cur[::-1]
    else:
        cur = cur + (cur[::-1])[1:]
    print(cur)
    #reset odd to False
    odd = False
    prev = cur
    cur = ""
"""
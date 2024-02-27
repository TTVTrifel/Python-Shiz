# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 01:29:54 2024

@author: omenc
"""
"""
a.
57 73 73 64 26 -108 79 -99 71 26 73 72 26 81 73 79 76 26 -109 69 64 78 65 76 -109 27

Good luck on your midterm!
"""
#You could not have made the instructions more difficult to understand


cipher = str(input("Input The Cipher Below \n"))
cipherList = cipher.split()
myList = []
myList2 = []
phrase = ""
for x in cipherList:
    a = int(x)
    if(a >= 0):
        a = oct(a)
        b = str(a)
        b = b[2:]
        b = int(b)
        myList.append(b)
    else:
        a = a * -1
        myList.append(a)
for y in myList:
    if y >= 0:
        phrase = phrase + str(chr(y))
print(phrase)



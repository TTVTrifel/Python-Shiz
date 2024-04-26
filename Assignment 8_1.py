# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:39:35 2024

@author: omenc
"""



"""
a.
There are 2 numeric characters: ['9', '2']
There are 5 lower case characters: ['n', 'w', 'e', 'd', 'k']
There are 5 upper case characters: ['V', 'P', 'A', 'A', 'E']
There are 4symbols: ['<', '}', '`', '?']

b.
There are 1 numeric characters: ['6']
There are 6 lower case characters: ['u', 'j', 'm', 'z', 'n', 'e']
There are 6 upper case characters: ['B', 'M', 'L', 'L', 'H', 'E']
There are 3symbols: ['@', '=', '"']

c.
There are 1 numeric characters: ['3']
There are 5 lower case characters: ['s', 'd', 't', 'm', 'z']
There are 4 upper case characters: ['K', 'U', 'G', 'W']
There are 6symbols: ['}', '?', '_', ':', '=', '+']

d.
There are 2 numeric characters: ['7', '2']
There are 5 lower case characters: ['p', 't', 'c', 'r', 'm']
There are 6 upper case characters: ['N', 'K', 'N', 'Y', 'P', 'S']
There are 3symbols: ['`', '/', '/']

e.
There are 2 numeric characters: ['5', '6']
There are 2 lower case characters: ['k', 'a']
There are 5 upper case characters: ['K', 'V', 'E', 'A', 'B']
There are 7symbols: ['^', '&', '!', '?', '`', '@', '$']






"""
numeric = []
lower = []
upper = []
symbol = []
my_Input = str(input("weird phrase:\n"))

def WordStuff(word):
    for i in range(0,len(word)):
        if str(word[i]).isnumeric():
            numeric.append(word[i])
    for i in range(0,len(word)):
        if str(word[i]).islower():
            lower.append(word[i])
    for i in range(0,len(word)):
        if str(word[i]).isupper():
            upper.append(word[i])
    for i in range(0,len(word)):
        if str(word[i]).isalnum() == False:
            symbol.append(word[i])
            
    num = "There are " + str(len(numeric)) + " numeric characters: " + str(numeric) + "\n"
    low = "There are " + str(len(lower)) + " lower case characters: " + str(lower) + "\n"
    up = "There are " + str(len(upper)) + " upper case characters: " + str(upper) + "\n"
    sym = "There are " + str(len(symbol)) + "symbols: " + str(symbol) + "\n"
    answer = num + low + up + sym
    return answer
    




print(WordStuff(my_Input))


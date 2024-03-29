# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:28:35 2024

@author: omenc
dude this took forever
"""


    


def Permutate(word):
    if(len(word) == 1):
        return [word]

    my_list = []

    for i in range(len(word)):
        start = word[i]
        #       all after + all before
        others =  word[:i] + word[i+1:]
        for rest in Permutate(others):
            my_list.append(start + rest)
    
    return my_list
    

my_input = str(input("Input a String:\n"))
print(Permutate(my_input))

















"""

1234
    1342
        1324
    1423
        1432
    1234
        1243
2341
    2413
        2431
    2134
        2143
    2341
        2314
3412
    3124
        3142
    3241
        3214
    3412
        3421
4123
    4231
        4213
    4312
        4321
    4123
        4132
    

1
    2
        3   4
        4   3
    3
        2   4
        4   2
    4
        2   3
        3   2
2
    1
        3   4
        4   3
    3
        1   4
        4   1
    4
        1   3
        3   1
3
    1
        2   4
        4   2
    2
        1   4
        4   1
    4   
        1   2
        2   1
4
    1
        2   3
        3   2
    2
        1   3
        3   1
    3   
        1   2
        2   1
    """
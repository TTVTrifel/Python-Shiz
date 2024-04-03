# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:35:55 2024

@author: omenc
"""

my_input = str(input("verse:\n"))
my_common = int(input("common:\n"))
def NLP (string, Common = 0):
    my_count = []
    string = string.replace("\n"," ")
    string = string.lower()
    string = " " + string + " "
    my_List = list(string.split(" "))
    my_List = list(set(my_List))
    my_List = my_List[1:]
    #print(my_List)
    
    for i in range(0,len(my_List)):
        word = str(my_List[i])
        my_count.append((string.count(str(" " + word + " "))))
        #print(" " + word + " ")
        #print(my_count[i])
     #number of unique words   
    print(str(len(my_List)) + " Unique Words")
    n_list = my_List
    n_count = my_count
    
    if(Common > 0):
        for a in range(0,Common):
            
            my_index = (n_count.index(max(n_count)))
            my_word = (n_list[my_index])
            print(str(my_word) + " occurs " + str(n_count[my_index]) + " times")
            
            n_list = n_list[:my_index] + n_list[my_index + 1:]
            n_count = n_count[:my_index] + n_count[my_index + 1:]
            
NLP(my_input, my_common)
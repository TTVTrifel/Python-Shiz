# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:10:57 2024

@author: omenc
"""
"""
a.
SATOR


b.
ELIZABETH


"""





newWord = ""
my_list = []
answer = ""
word = ""
my_input = str(input("acrostic"))

x = 0
word = my_input

word = word.replace("\\n","")
#word = word.replace("\\","")
word = word.replace("\\t","")
words = word.split("\n")

for i in words:
    for x in i:
        if(x.isalnum() == True):
            newWord = newWord + x
    my_list.append(newWord)
    newWord = ""


for i in range(0,len(my_list)):
    word = str(my_list[i])
    try: answer = answer + word[0]
    except:
        pass
print(answer)


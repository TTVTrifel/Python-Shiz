# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 00:31:10 2024

@author: omenc
"""

#Questions
"""
a. 1, 10, 1

The Mean of Your Integers is 4.0

The Median of Your Integers is 10

The range of Your Integers is 9

b. 1, 5, 3

The Mean of Your Integers is 3.0

The Median of Your Integers is 5

The range of Your Integers is 4

c. 10, 1, -1

The Mean of Your Integers is 3.3333333333333335

The Median of Your Integers is 10

The range of Your Integers is 11

d. 1, 10, -1

The Mean of Your Integers is 3.3333333333333335

The Median of Your Integers is 10

The range of Your Integers is 11

"""

#ask the user to input numbers, after 3, have it ask if they want to input more
#then if no more, those numbers are added into an index 
#that index is then sorted least to greatest.

i = 0
myList = []
done = False
mean = 0
median = 0
myRange = 0
print("input as many integers as you want, as least 3 times\nthen the program will find the mean, median, and range\n")
while(done == False):
    if(i >= 3):
        Query = (input("type 'Done' if finished, or input another integer\n"))
        if(Query == "Done"):
            break
        else: Query = int(Query)
    else:
        Query = int(input("Input An Integer Below:\n"))
    myList.append(Query)
            
    i = i + 1
myList.sort()
print("Your list is: " + str(myList))

#from there 3 different functions take place, mean, median, and range

#1
for x in myList:
    mean = mean + x
mean = mean / len(myList)
print("\nThe Mean of Your Integers is " + str(mean))

#2
median = int(myList[(int(round((len(myList) / 2))))])
print("\nThe Median of Your Integers is " + str(median))

#3
myRange = int(myList[-1]) - int(myList[0])
print("\nThe range of Your Integers is " + str(myRange))
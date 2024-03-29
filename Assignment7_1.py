# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:44:33 2024

@author: omenc
"""

def Dice_Prob (dice_config, val):
    #for dice_config please use the form " 2d6 " or " 1d20 "
    try:
        if(dice_config[1] != "d"):
            return "please use correct formatting for dice_config"

        dice_amount = int(dice_config[0])

        dice_sides = int(dice_config[2:])
        if(val < dice_amount):
            return "please input a val greater than the amount of dice"
        val_list =[]
        for i in range(dice_amount, int((dice_amount * dice_sides) + 1)):
            if(i >= val):
                val_list.append(i)
        if(type(val) != int):
            return "please input an int for val"
        print(str(len(val_list)) + "/" + str((dice_amount * dice_sides) - (dice_amount - 1)))
    except:
        print("error! please input correct values in the correct format")
    
    
    
    
    
    
Dice_Prob("2d6", 7)
Dice_Prob("2d6", 9)
Dice_Prob("3d8", 22)
Dice_Prob("1d20", 17)
Dice_Prob("6", 5)

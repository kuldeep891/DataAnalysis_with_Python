# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 14:35:01 2019

@author: KUKUMAR
"""

def menu(items):
    for i in range(len(items)):
        print(items[i])
    #sample = 'Kuldeep'    
    choice = int(input("Enter the option : "))
    return choice

choice = 0
mlist = ["1.Add","2.Update","3.Remove","4.Display"]
while ( choice < 5 ):
    print(choice)
    choice = menu(mlist)
    print(choice,"value of choice")
    print(choice)
    if(choice == 1):
        print("Selected option is ",choice)
    elif (choice == 2):
        print("Selected option is ",choice)
        mlist.append("5.Extra Option")
    elif (choice == 3):
        print("Selected option is ",choice)
    elif (choice == 4):
        print("Selected option is ",choice)
    else:
        print("Menu in Progress")
    
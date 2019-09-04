# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 13:48:10 2019

@author: KUKUMAR
"""
f = None

try:
    try:
        f = open(r"C:\Users\kukumar\Documents\GitHub\LearningPython\c.txt","r")
    except IOError:
        print("File doesnt exist \n")
        fname = input("Enter Valid Filename ")
        f = open(fname,"r")
    data = f.readlines()
    for i in range(len(data)):
        line = data[i]
        line=line.replace("\n","")
        #print(line)
        temp = line.split(" ")
        print(temp[1])
        f.close()
except IndexError:
    print("Check Data Source, Issue with Index Out of Bound ")
except IOError:
    print("File doesnt exist \n")

print("Hello")    
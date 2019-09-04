# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 14:16:04 2019

@author: KUKUMAR
"""
import pandas as pd
import numpy as np

stop_words = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Sentiment Analysis\stop-word-list.csv')
positive = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Sentiment Analysis\positive.csv')
negative = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Sentiment Analysis\negative.csv')

stp=list(stop_words.Values)
#list_stop = stop_words.values.tolist()
#print(stop_words['Values'])

data = input("Enter the Paragraph : \n")

l1 = data.split(' ')

'''
for i in stop_words['Values']:
    if i in l1:
#        print(i)
        l1.remove(i)
'''
found=[]
for i in l1:
    if i in stp:
        found.append(i)
for item in found:
    l1.remove(item)

print("After removing Stop Words :\n",l1)

pflag=None
nflag=None

for i in l1:
    if i in positive['Values'].values.tolist():
        pflag = True
    elif i in negative['Values'].values.tolist():
        nflag = True

#print(pflag)
#print(nflag)


if(nflag == True and pflag == True):
    print("Neutral Sentiments")
elif(nflag == True):
    print("Negative Sentiments")
elif(pflag == True):
    print("Positive Sentiments")
else:
    print("Invalid Input")


#print(type(stop_word))

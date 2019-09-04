# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:15:34 2019

#####------Decision Tree------#####

Entropy             : proability of Uncertainty
Information gain    : Lesser the Entropy greater the information gain
Guniea Index        : 
# We need to get the path which has lesser uncertainty and maximum information gain

#Prog : Find the Features, check manually with the values for which the entropy is least
        Split them into nodes
        Calculate Entropy from scratch
        Now check from which node the entropy is least
        Use MAtplotlib to visualize the data
        Manual Trial and Error
    
@author: KUKUMAR
"""
import pandas as pd

data = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Entropy&InforGain\loan.csv')
print(data)

print(data.loc[data.creditscore >= 650])

#df = pd.DataFrame()

#df.loc[df.emi<=1000]
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 14:25:38 2019

@author: KUKUMAR
"""

import pandas as pd

#pandas read_csv will convert the csv file into DataFrames
data = pd.read_csv(r"C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Day5 Linear Regression\year_age_v1.csv")

print(data)

#data.year will be Float since it contains NAN values
#data.age doesnt have NAN hence its int64
#print(data.year)


#it will drop the rows with NAN values
data2 = data.dropna()

print(data2)

#data3 = data.dropna(axis=0,how='all')
#   will drop the rows with all values as None or NaN
#data3 = data.dropna(axis=0,how='any')
#   will drop the rows with any value as None or NaN

data3 = data.dropna(axis=0,how='any')

print(data3)

#################################################################

print(data)

#pad method will fill the NaN value with the previous value
data2 = data.fillna(method="pad")

#ffill will fill with the previous value
#fill value to next NaN
data2 = data.fillna(method="ffill")

#backfill will fill with the next value
#fill value to previous NaN
data2 = data.fillna(method="backfill")

print(data2)





























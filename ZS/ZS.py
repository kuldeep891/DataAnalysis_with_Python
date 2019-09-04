# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:16:41 2019

@author: KUKUMAR
"""
import pandas as pd
import os

raw_data_path = os.path.join(os.path.pardir,'data','raw')
train_data_path = os.path.join(raw_data_path,r"C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\ZS\Cristano_Ronaldo_Final_v1\data.csv" )
data = pd.read_csv(train_data_path, index_col=None)


print(len(data))

data.drop_duplicates()

print(len(data))


print(data.columns.duplicated())
#print(data)

#print(data.info())
trainingSet = data[data.is_goal.notnull()]
testData = data[data.is_goal.isnull()]

#print(trainingSet.duplicated())

#if(trainingSet.columns.duplicated()):
#    print("Duplicate records")

print("Count data          :\t",data.shape)
print("Count data not null :\t",trainingSet.shape)
print("Count data not null :\t",testData.shape)

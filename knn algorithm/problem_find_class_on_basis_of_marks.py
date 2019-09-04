# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:15:04 2019

@author: KUKUMAR

Candidate belong to which class, distinction, 1st, 2nd
sub1, sub2, sub3, sub4, sub5, class

40 % pass
"""
import pandas as pd
import numpy as np
import os

def eucleduian_distance():
    None

#set the raw data path, use os.path.join so that code can work on both Unix and windows
raw_data_path = os.path.join(os.path.pardir,'data','raw')
train_file_path = os.path.join(raw_data_path,r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\knn algorithm\sub_marks.csv')

data = pd.read_csv(train_file_path)

print(data)

data.info()

#print(data[1])

testSet = [40,42,48,35,32]
testData = pd.DataFrame(testSet)



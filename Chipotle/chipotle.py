# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 15:52:59 2019

@author: KUKUMAR
"""

import pandas as pd

data = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Chipotle\chipotle.tsv',sep = '\t')

#Check first five entries
print(data.head(5))

#Number of observations in the dataset
print(data.shape[0])


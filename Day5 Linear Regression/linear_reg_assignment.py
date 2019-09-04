# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:39:40 2019

@author: KUKUMAR
"""

'''
Assignment : 
    Implement Age and Year program
    Under supervised learning, train with the dataset and then check perfect the output is by
    comparing the data used to train.
'''

import pandas as pd
import numpy as np
from sklearn import linear_model

data = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Day5 Linear Regression\year_age_v1.csv');
#print(data)

data3 = data.dropna(axis = 0, how = 'any')
print(data3)

#x=np.array(data3['year']).reshape(-1,1)
x = data3['year']
y = data3['age']

regr = linear_model.LinearRegression()
regr.fit(x,y)

print('Intercepts   :\t',regr.intercept_)
print('Coefficients :\t', regr.coef_ )












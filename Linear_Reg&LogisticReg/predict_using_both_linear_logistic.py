# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:35:48 2019

@author: KUKUMAR
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import accuracy_score 

data = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Linear_Reg&LogisticReg\train.csv')
print(data)

x = data[['defaulter','income','expenses','cc','loan_applied']]
y = data['status']

regr = linear_model.LinearRegression()
regr.fit(x,y)

#print("Intercepts: \t",regr.intercept_)
#print("Coeff :\t",regr.coef_)

test_data = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Linear_Reg&LogisticReg\test.csv')
#print(test_data)

x_test = test_data[['defaulter','income','expenses','cc','loan_applied']]
#print(x_test)

ypred=regr.predict(x_test)
print(ypred)
'''
print(x_test.length())
for i in range(x_test):
    print("Prediction for :",x_test.iloc[i]," is : \t",ypred.iloc[i])
    '''
x_test = test_data[['loan_applied']]
logreg=linear_model.LogisticRegression()
logreg.fit(x_test,y)

ypred_log=logreg.predict(x_test)
print(ypred_log)

print("model accuracy is",accuracy_score(y,ypred_log))


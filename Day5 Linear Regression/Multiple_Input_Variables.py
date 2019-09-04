# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 14:21:50 2019

@author: KUKUMAR
"""
from pandas import DataFrame
from sklearn import linear_model

#import matplotlib.pyplot as plt
#import scikit_learn.linear_model as lm

#data = pd.read_csv(r"C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Day5 Linear Regression\dataset_multiple_variable.csv")

Stock_Market = {
        'Year':[2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
        'Month':[12,11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5],
        'Interest_Rate':[2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2.25,2.25,2.25,2.25,2,2,1.6,1.6],
        'Unemployment_Rate':[5.3,5.4,5.4,5.4,5.5,5.6,5.7,5.8,5.9,6,6,6.1,6.1,6.1,6.2,6.2,6.2,5.9,6,6.1],
        'Stock_Index_Price':[1464,1245,1026,807,588,1117,1010,1111,1340,1250,1420,1000,980,970,876,999,976,1006,1200,1216]
        }

df = DataFrame(Stock_Market,columns=['Year','Month','Interest_Rate','Unemployment_Rate','Stock_Index_Price'])

x = df[['Interest_Rate','Unemployment_Rate']]
#x = df['Interest_Rate','Unemployment_Rate']
y = df['Stock_Index_Price']

#Using Sklearn

regr = linear_model.LinearRegression()
regr.fit(x,y)

print('Intercept    : ',regr.intercept_)
print('Coefficients : ',regr.coef_)


#prediction using sklearn
new_int_rate = 2.75
new_unemp_rate = 5.3
print('Predicted Stock Index Price : ',regr.predict([[new_int_rate,new_unemp_rate]]))
#print('Predicted Stock Index Price : ',regr.predict([new_int_rate,new_unemp_rate]))
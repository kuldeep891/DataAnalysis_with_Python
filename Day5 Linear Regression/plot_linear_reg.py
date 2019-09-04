# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 15:04:13 2019

@author: KUKUMAR
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#pandas read_csv will convert the csv file into DataFrames
data = pd.read_csv(r"C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Day5 Linear Regression\year_age_v1.csv")
#print(data)

data3 = data.dropna(axis=0,how='any')
print(data3)

plt.plot(data.year,data.age)
plt.show()


data2 = data.fillna(method="backfill")
plt.plot(data2.year, data2.age)
plt.show()

'''data3 = data.fillna(method="ffill")
plt.plot(data3.year, data3.age)
plt.show()
'''


def estimate_coef(x,y):
    #number of observations/points
    n = np.size(x)
    print(n)
    #mean of x and y yector
    m_x, m_y = np.mean(x), np.mean(y)
    #calculating cross-deviation and deviation about x
    SS_XY = np.sum(y*x) - n*m_y*m_x
    SS_XX = np.sum(x*x) - n*m_x*m_x
    #calculating regression coefficients
    m=SS_XY / SS_XX
    b=m_y - m*m_x
    return b,m

x=np.array(data3.year)
y=np.array(data3.age)
b,m = estimate_coef(x,y)
print("Estimated coefficients : b=",b," m = ",m)
x1=int(input("Value of X:"))
print(m)

y1=m*x1+b
print(y1)
    
    
    
    
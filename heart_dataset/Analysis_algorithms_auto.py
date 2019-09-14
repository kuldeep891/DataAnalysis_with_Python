# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:59:34 2019

@author: KUKUMAR
Q : Whats the funda for pass by reference in dataframes, as below changed the main dataframe
"""

# Import All Required Packaged here
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings('ignore')


def data_preprocessing(data,i_output,i_method):
    #cols = data.columns.tolist()
    data.fillna(method = i_method,inplace = True)
    X = data.drop([i_output],axis = 'columns')
    Y = data[i_output].values
    #Use Standard Scaler to Scale the Dataset
    sc = StandardScaler()
    x  = sc.fit_transform(X)
    return train_test_split(x,Y,random_state= 100,test_size = 0.2)
    #return x_train,x_test,y_train,y_test
    
    
def logistic_regression(x_train,x_test,y_train,y_test):
    logreg = LogisticRegression()
    logreg.fit(x_train,y_train)
    y_pred = logreg.predict(x_test)
    return accuracy_score(y_test,y_pred)

def knn_classifier(x_train,x_test,y_train,y_test):
    knn = KNeighborsClassifier()
    knn.fit(x_train,y_train)
    y_pred = knn.predict(x_test)
    return accuracy_score(y_pred,y_test)
    
def decision_tree():
    None

def random_forest():
    None



if __name__ == '__main__' :
    data = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\DataAnalysis_with_Python\heart_dataset\heart_dataset_updated.csv')
    x_train,x_test,y_train,y_test = data_preprocessing(data,'target','ffill')
    print(logistic_regression(x_train,x_test,y_train,y_test),knn_classifier(x_train,x_test,y_train,y_test))

    #print(x_train)
    #print(data.isnull().sum())
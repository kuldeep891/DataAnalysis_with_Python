# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 15:08:48 2019

@author: KUKUMAR
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\Entropy&InforGain\loan.csv')
#print(data)
X = data.drop(['loanamount','approval'],axis = 1)
Y = data['approval']
print(X)

x_train,x_test, y_train,y_test = train_test_split(X,Y,test_size = 0.90)
classifier = DecisionTreeClassifier()
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)

datas = pd.DataFrame({'Actual':y_test,'Predicted':y_pred})

print('Train DataSet : \n',data.loc[x_train.index].loc[data.approval ==1])
print('Test DataSet : \n',data.loc[x_test.index])
print('Predicted Values : \n',y_pred)

print('Accuracy',metrics.accuracy_score(y_test,y_pred))
#print(data)



'''
Confusion Matrix
sklearn classes and libraries

train_test_split
Decision_tree_classifier
metrix

'''
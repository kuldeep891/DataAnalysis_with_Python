# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:40:39 2019

@author: KUKUMAR
"""

import pandas as pd
import numpy as np


#dist = eucledian_dist(testInstance, trainingSet.iloc[i], length)
def eucledian_dist(data1, data2, length):
    distance = 0
    for i in range(length):
        distance += np.square(data1[i] - data2[i])
    print("distance of ",data1," with ",data2," is :\n",np.sqrt(distance))
    return np.sqrt(distance)

def knn(trainingSet,testInstance, k):
    distances = {}
    length = testInstance.shape[1]
    #.shape function tells us the total number of dimensions
    print("Total Dimensions are : ",length)
    for i in range(len(trainingSet)):
        dist = eucledian_dist(testInstance, trainingSet.iloc[i], length)
        distances[i] = dist[0]
    print("dist items are ",distances.items())
    sorted_d =  sorted(distances.items(), key = lambda elem: elem[1])
    print("sorted dists : ")
    neighbours = []
    for i in range(k):
        neighbours.append(sorted_d[i][0])
    classvotes = {}
    for i in range(len(neighbours)):
        response = trainingSet.iloc[neighbours[i]][-1]
        if response in classvotes:
            classvotes[response] += 1
        else:
            classvotes[response]  = 1
    sortedvotes = sorted(classvotes.items(), key = lambda elem: elem[1], reverse = True)
    return sortedvotes[0][0], neighbours


data = pd.read_csv(r'C:\Users\kukumar\OneDrive - AMDOCS\Backup Folders\Documents\GitHub\LearningPython\knn algorithm\xy_cordinates.csv')
print(data)

testSet = [142,58,32]
test = pd.DataFrame(testSet)
k = 3
result, neigh = knn(data, test, k)
print(result)
print(neigh)

#x=np.array(data['height']).reshape(-1,1)
#print(x)
#print(y)



# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:24:43 2019

@author: KUKUMAR
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

import matplotlib.style as style
style.use("ggplot")

data = [[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]]

x = np.array(data)

kmeans = KMeans(n_clusters = 2)
kmeans.fit(x)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

# g is green color and . is symbol type can also be + #
colors = ["g+","r.","c.","y."]

xtest = int(input("Enter X : \n"))
ytest = int(input("Enter Y : \n"))

values = kmeans.predict([[xtest,ytest]])

#print(kmeans.score(x))

print(values)
print(type(values))

'''
data.append([xtest,ytest])
x = np.array(data)

kmeans = KMeans(n_clusters = 2)
kmeans.fit(x)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_
'''
for i in range(len(x)):
    print("co-ordinate:  ",x[i], "labels : ",labels[i])
    plt.plot(x[i][0], x[i][1], colors[labels[i]],markersize = 10)

plt.scatter(centroids[:,0],centroids[:,1],marker = "x")
plt.plot(xtest,ytest,colors[values[0]],markersize = 10)
plt.show()
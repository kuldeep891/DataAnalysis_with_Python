# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:36:55 2019

@author: KUKUMAR
"""
import numpy as np

def calc_mean_chk(mm,val):
    if( np.absolute(mm[0] - val) <   np.absolute(mm[1] - val)):
        m1.append(val)
    else:
        m2.append(val)

def mean_modify(m,m1,m2):
    del m[:]
    m.append(np.mean(m1))
    m.append(np.mean(m2))

def move_cluster(m,m1,m2):
    flag = 0
    print("in move_cluster")
    for i in m1 :
        if(np.absolute(i - m[0]) > np.absolute(i - m[1])):
            flag = 1
            m2.append(i)
            m1.remove(i)
            mean_modify(m,m1,m2)
    for i in m2 :
        if(np.absolute(i - m[0]) < np.absolute(i - m[1])):
            flag = 1
            m1.append(i)
            m2.remove(i)
            mean_modify(m,m1,m2)

    return flag


# 1D dataset for clustering       
l_dataset = [1,8,2,6,3,1,9,7,8,2,9]
#l1 = [40, 20, 30, 10, 22, 94, 66]

#number of clusters
k=int(input("Enter the k value : \n"))

m_mean=list()
k_cluster=list()

m1=list()
m2=list()


i=0
while i<k_cluster:
    m.append(l_dataset[i])
    i+=1

#Clustering Process
for i in l1:
    calc_mean_chk(m,i)
    mean_modify(m,m1,m2)
    
#Re CLustering
while (move_cluster(m,m1,m2) != 0):
    None
    
print("Mean      : ",m)
print("CLuster 1 : ",m1)
print("Cluster 2 : ",m2)

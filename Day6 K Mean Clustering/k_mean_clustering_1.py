# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:12:10 2019

@author: KUKUMAR
"""

# K means clustering

import numpy as np

def calc_mean_chk(m_list,val1):
    check = list()
    for i in m_list:
        check.append(np.absolute(i-val1))
    
    #range = len(check)
    
    i =0
    if np.absolute(check[i] - m_list[i]) < np.absolute(check[i+1]-m_list[i+1]):
        m1.append(val1)
    else:
        m2.append(val1)

def modify_mean(m11,m22,m):
    mm1 = np.mean(m11,axis = None)
    mm2 = np.mean(m22,axis = None)
    
    del m[:]
    m.append(mm1)
    m.append(mm2)
    

'''
def add_to_cluster(mk_list, diff_list, val):
    range = len(mk_list)
    i=0
    flag = 0
    if(np.absolute(diff_list(i) - mk_list(i)) < np.absolute(mk_list(i+1) - diff_list(i+1))):
        m1.append()
    else:
        None
  '''  

l1 = [1,8,2,6,3,1,9,7,8,2,9]
k = int(input('Enter the number of clusters required :\n'))

#List for mean of n number of clusters 
m=list()

m1 = list()
m2 = list()

i=0
#print(type(i))
#print(i)

while i<k:
    m.append(l1[i])
    i+=1

print("MEan List : ",m)
print ( "NExt VAlue : ",l1[k+0])

diff = calc_mean_chk(m,l1[k+0])
print("abs value : ", diff)

for i in l1:
    calc_mean_chk(m,i)
    modify_mean(m1,m2,m)
    

print(m1)
print(m2)

#add_to_cluster(mean , difference, value )
#add_to_cluster(m, diff , l1[k+0])









    

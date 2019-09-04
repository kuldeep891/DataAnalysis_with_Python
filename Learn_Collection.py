# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:34:12 2019

@author: KUKUMAR
"""

a=[True,True,False,True]
b=['a','b','c','d']

dic = {}
list1 = []
#{'a':[0,1,3], 'b':[0,1,3],'c':[0,1,3],'d':[0,1,3]}

print ({b[idx]:a for idx,i in enumerate(b) 
                  })




"""

for i in range(len(a)):
    for j in range(len(a)):
        if ( a[j] ):
            list1.append(j)
    dic[b[i]] = list1
    list1 = []
    
print (dic)"""
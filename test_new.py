# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:04:24 2019

@author: KUKUMAR
"""



def num_sum(a,b):
    return a+b
    
#a = int(input("Enter a number :"))
#b = int(input("Enter a number :"))

#print(num_sum(a,b))

l1 = [1,2,3,4,'kuldep',12.34]
d1 = {"kul":[1,2,3], "push":[4,5,6]}

ld = {"A1":{"B1":[12,34],"B2":[23]},"A2":{'C1':[120,340],"C2":[230]}}

print("Lists:\n")
print(l1)
print(type(l1))


print("\nDistcionary:\n")
print(d1)
print(type(d1))

print("\nDistcionary:\n")
print(ld)
print(type(ld))

del ld['A2']
print(ld)


#print(a)
#print("Type : ", type(a))

    
    





# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:42:50 2019

@author: KUKUMAR
"""

def banner(message, border = '-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

if __name__ == '__main__':
    banner(border = "#",message="Kuldeep",)

a = 10

print(a)
print(id(a))

b = 10

print(b)
print(id(b))

print(a==b)
print(id(a)==id(b))

 
print(a is b)
print(id(a) is id(b))


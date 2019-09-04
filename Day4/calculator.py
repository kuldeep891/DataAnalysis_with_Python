# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:25:44 2019

@author: KUKUMAR
"""

def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b=1):
    return a/b

def main():
    try : 
        operand = ('(',')','/','*','+','-')
        print("Enter the calculation sequence followed by Enter : \n Consequent Enter will end your calculations ")
        a = float(input())
        op = input()
        b = float(input())
        while True:
            if (op in operand):
                if (op == '+'):
                    out = sum(a,b)
                elif (op == '-'):
                    out = subtract(a,b)
                elif (op == '*'):
                    out = multiply(a,b)
                elif (op == '/'):
                    out = divide(a,b)
                else:
                    print("Invalid ")
            else:
                print("Invalid Operation ")
            print(out)
            a = out
            op = input()
            if (op == ''):
                print("Thank you")
                break
            b = float(input())
    except ValueError:
        print("ValueError Enter Correct Value")

if __name__ == "__main__":
    main()
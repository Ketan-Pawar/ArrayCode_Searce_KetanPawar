# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 20:23:03 2022

@author: Sanjay
"""

# Using for loop
# a = []
# count = int(input("Enter the size of an array: "))

# for i in range(0,count):
#     l = int(input())
#     a.append(l)
# print(a)

# By using slicing
# a = int(input("Number of elements in an array: "))
# num = list(map(int, input("Enter an elements: ").strip().split()))
# print("Entered array is : ",num)
# print("Reversed array is : ",num[::-1])

# By using reverse function
a = int(input("Number of elements in an array: "))
num = list(map(int, input("Enter an elements: ").strip().split()))
print("Entered array is : ",num)
num.reverse()
print("Reversed array using Reverse Function: ",num)


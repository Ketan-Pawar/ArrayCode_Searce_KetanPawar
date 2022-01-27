# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 20:43:56 2022

@author: Sanjay
"""

arr = [5, 2, 8, 7, 1];     
temp = 0;    
     
#original array    
print("Elements of original array: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
     
#Sorting array in ascending order    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print()
     
#Displaying after sorting    
    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 20:31:23 2022

@author: Sanjay
"""

# Selection sort 

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [10, 2, 0, -1, 4, 7]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
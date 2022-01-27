# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:15:48 2022

@author: Sanjay
"""

import array
 
s1 = array.array('i', [1, 2, 3])
s2 = array.array('i', [4, 5, 6])
 
print(s1)  
print(s2)  
 
s3 = s1 + s2
print(s3)  
 
s1.append(4)
print(s1)  
 
s1.insert(0, 10)
print(s1) 
 
s1.extend(s2)
print(s1) 
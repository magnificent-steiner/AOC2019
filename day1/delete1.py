# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:01:04 2019
day 1
"""
import numpy as np

f= open("delete1.txt", "r+")        #as it is in same dirertory
sum=0.0

for x in f:
    mass=int(x)
    sum+=((np.floor(mass/3))-2)

print(sum)

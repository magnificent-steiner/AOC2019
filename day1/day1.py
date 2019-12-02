# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:01:04 2019
day 1
"""
import numpy as np

f= open("delete1.txt", "r+")        #as it is in same dirertory
sum=0.0

 
def extra_fuel(m):
    s=0.0
    fl=((np.floor(m/3))-2)      #preliminary test
    while(fl>0):
        s+=fl
        fl=((np.floor(fl/3))-2)
        
        
    return (s)

for x in f:
    mass=int(x)
    fuel=((np.floor(mass/3))-2)
    efuel=extra_fuel(fuel)
    sum+=fuel+efuel
    

#print(fuel)      #answer to part 1

print(sum)
    
    



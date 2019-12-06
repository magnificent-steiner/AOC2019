# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:11:52 2019

orbit
"""

import numpy as np

f=open("day6.txt", 'r+')
orbit=f.read().split("\n")
#print(orbit)    


def recurse_dist(x):      
    global ct
    if(keys[values.index(x)]=='COM'):
        return (ct) 
    else:
        ct+=1        
        return (recurse_dist(keys[values.index(x)]))
            
        
orblist=[]
for x in orbit:
    a=(x.split(")"))
    orblist.append((a[0], a[1]))

#print(orblist)       
    
values=[]
keys=[]
for a in orblist:
    #print(a[0],a[1])
    values.append(a[1])#for all values, search recursively until key becomes COM
    keys.append(a[0])
    
sum=0
for x in values:
    ct=1
    sum+=(recurse_dist(x))
    
print(sum)
 
        

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:27:25 2019

orbit part2
"""

import numpy as np

f=open("day6.txt", 'r+')
orbit=f.read().split("\n")
   

def recurse_dist2(x,path):      
    #global path1
    if(keys[values.index(x)]=='COM'):
        return (path) 
    else:       
        path.append(keys[values.index(x)])
        #path.append(keys[values.index(x)])
        return (recurse_dist2(keys[values.index(x)],path))
            
        
orblist=[]
for x in orbit:
    a=(x.split(")"))
    orblist.append((a[0], a[1]))
      
    
values=[]
keys=[]
for a in orblist:
    values.append(a[1])
    keys.append(a[0])
    
    
path1=[]
recurse_dist2('YOU',path1)

path2=[]
recurse_dist2('SAN',path2)

res = list(set(path1)^set(path2))
print(len(res))             #part2 ans

    
        

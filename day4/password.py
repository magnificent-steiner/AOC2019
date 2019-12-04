# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:46:11 2019

password criteria
"""

#consecutive
def criteria1(x):
    flag=0
    sx=str(x)
    for i in range(5):
        if(sx[i]==sx[i+1]):
            flag=1
    return(flag)

#never decrease
def criteria2(x):
    flag=1
    sx=str(x)
    for i in range(5):
        if(sx[i+1]<sx[i]):
            flag=0

    return(flag)



nos=[]          #keep subset of part1 answers
for x in range(193651,649729):
    if(criteria1(x) and criteria2(x)):
        nos.append(x)

print(len(nos))            #part1 ans

#consecutive are only 2 in nos.
def criteria3(x):
    flag=0
    s=str(x)
    for i in range(5):
        if(s[i]==s[i+1]):
            if((i==0 or s[i]!=s[i-1]) and (i==4 or s[i+2]!=s[i+1])):
                flag=1

    return(flag)


c=0
for x in nos:
    if(criteria3(x)):
        c+=1

print(c)               #part2 ans

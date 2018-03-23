#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:06:36 2018

@author: shubhamsinha
"""

import numpy as np
#from random import shuffle, randrange
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot

def visit(x,y):
    stack=[]
    stack.append((x,y))
    visited[x][y]=1
    blocked[x][y]=0
    count=0
    while (1)  : 
        count=count+1     
        neighbours=[]
        if (x > 0 and visited[x-1][y]==0):       
                neighbours.append((x-1,y))
        if x < size-1 and visited[x+1][y]==0:        
                neighbours.append((x+1,y))
        if y > 0 and visited[x][y-1]==0:          
                neighbours.append((x,y-1))
        if y < size-1 and visited[x][y+1]==0:       
                neighbours.append((x,y+1))
        if len(neighbours)==0 and len(stack)==0:
            break
        if len(neighbours):
            x_,y_ = neighbours[rand(0, len(neighbours) - 1)]
            
            block_=np.random.choice([0,1], p=[0.7, 0.3])
            
            if block_==1:
                blocked[x_][y_]=1
                visited[x_][y_]=1
            else:
                blocked[x_][y_]=0
                visited[x_][y_]=1
                stack.append((x_,y_))
                x,y=x_,y_
          
        else:
            if(len(stack)!=0):
                 x,y= stack.pop()
    print('count: ',count )
    
    
size=101
visited=np.zeros((size,size), dtype=int)
blocked=np.empty((size,size), dtype=int)

print(blocked)


initial_i=np.random.randint(0,size-1)
initial_j=np.random.randint(0,size-1)
print(initial_i)
print(initial_j)



x=initial_i
y=initial_j

#print(stack)


 
visit(x,y)

for x in range(0, size):
    for y in range(0, size):
        if visited[x][y]!=1:
            print('unvisited: ',x,y,visited[x][y])
            visit(x,y)
    
#numpy.where(array==item)

pyplot.figure(figsize=(10, 10))
pyplot.imshow(blocked, cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()

for x in range(0, size):
    for y in range(0, size):
        if blocked[x][y]!=1 and blocked[x][y]!=0:
            print('incomplete', x,y,blocked[x][y])
            break
    break

print (blocked)
print (visited)
#np.save('maze50.npy', blocked)
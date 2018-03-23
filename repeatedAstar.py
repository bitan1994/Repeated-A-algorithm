#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:39:02 2018

@author: shubhamsinha
"""

import numpy as np
import math
from heapq import *
import sys
import matplotlib.pyplot as pyplot
MAX_INT= 2147483647

def heuristic(a):
    (x1,y1)=a
    #(x2,y2)=b
    return abs(x1-target_x)+abs(y1-target_y)

def backtrace(parent, start, end):
    path = [end]
    print("in backtrace")
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    print("path done")
    return path

def getfromOpenlistGreater():
    if len(openlist)==0:
        return null
    minimum=min(openlist)[0]
    minimum_x=min(openlist)[1][0]
    minimum_y=min(openlist)[1][1]
    for count,open in enumerate(openlist): 
                    if open[0]==minimum and g[open[1][0]][open[1][1]]>g[minimum_x][minimum_y]: 
                        #print('nohhh')
                        minimum_x=open[1][0]
                        minimum_y=open[1][1]
    for count,open in enumerate(openlist): 
                    if open[1][0]==minimum_x and open[1][1]==minimum_y: 
                        #print('nohhh')
                        openlist[count] = openlist[-1]
                        openlist.pop()
                        heapify(openlist)
    return (minimum_x,minimum_y)

def getfromOpenlistLesser():
    if len(openlist)==0:
        return null
    minimum=min(openlist)[0]
    minimum_x=min(openlist)[1][0]
    minimum_y=min(openlist)[1][1]
    for count,open in enumerate(openlist): 
                    if open[0]==minimum and g[open[1][0]][open[1][1]]<g[minimum_x][minimum_y]: 
                        #print('nohhh')
                        minimum_x=open[1][0]
                        minimum_y=open[1][1]
    for count,open in enumerate(openlist): 
                    if open[1][0]==minimum_x and open[1][1]==minimum_y: 
                        #print('nohhh')
                        openlist[count] = openlist[-1]
                        openlist.pop()
                        heapify(openlist)
    return (minimum_x,minimum_y)

def actions(a):
    valid=[]
    (x,y)=a
    if x>0 and knownblocked[x-1][y]!=1:
        valid.append((-1,0))
    if x<size-1 and knownblocked[x+1][y]!=1:
        valid.append((1,0))
    if y>0 and knownblocked[x][y-1]!=1:
        valid.append((0,-1))
    if y<size-1 and knownblocked[x][y+1]!=1:
        valid.append((0,1))
        
    return valid

def ComputePath1():
    print('in compute path')
    global counter
    global nexpanded
    while  len(openlist)!=0 and g[target_x][target_y]>min(openlist)[0] :
        s=getfromOpenlistGreater()
        #print(s)
        s_x=s[0]
        s_y=s[1]
        #print('expanding: ',s_x,s_y)
        closedlist.add((s_x,s_y))
        nexpanded+=1
        actionlists=actions((s_x,s_y))
        for action in actionlists:
            if search[s_x+action[0]][s_y+action[1]]<counter:
                g[s_x+action[0]][s_y+action[1]]=MAX_INT
                search[s_x+action[0]][s_y+action[1]]=counter
            if g[s_x+action[0]][s_y+action[1]]>g[s_x][s_y]+1:
                g[s_x+action[0]][s_y+action[1]]=g[s_x][s_y]+1
                #tree pointer
                tree[(s_x+action[0],s_y+action[1])]=(s_x,s_y)
                #check if in open list, if yes remove from openlist
                
                for count,open in enumerate(openlist): 
                    if open[1][0]==s_x+action[0] and open[1][1]==s_y+action[1]: 
                        #print('nohhh')
                        openlist[count] = openlist[-1]
                        openlist.pop()
                        heapify(openlist)
                
                f=g[s_x+action[0]][s_y+action[1]]+heuristic((s_x+action[0],s_y+action[1]))
                heappush(openlist,(f,(s_x+action[0],s_y+action[1])))
                
def ComputePath2():
    print('in compute path')
    global counter
    global nexpanded2
    while  len(openlist)!=0 and g[target_x][target_y]>min(openlist)[0] :
        s=getfromOpenlistLesser()
        #print(s)
        s_x=s[0]
        s_y=s[1]
        #print('expanding: ',s_x,s_y)
        closedlist.add((s_x,s_y))
        nexpanded2+=1
        actionlists=actions((s_x,s_y))
        for action in actionlists:
            if search[s_x+action[0]][s_y+action[1]]<counter:
                g[s_x+action[0]][s_y+action[1]]=MAX_INT
                search[s_x+action[0]][s_y+action[1]]=counter
            if g[s_x+action[0]][s_y+action[1]]>g[s_x][s_y]+1:
                g[s_x+action[0]][s_y+action[1]]=g[s_x][s_y]+1
                #tree pointer
                tree[(s_x+action[0],s_y+action[1])]=(s_x,s_y)
                #check if in open list, if yes remove from openlist
                
                for count,open in enumerate(openlist): 
                    if open[1][0]==s_x+action[0] and open[1][1]==s_y+action[1]: 
                        #print('nohhh')
                        openlist[count] = openlist[-1]
                        openlist.pop()
                        heapify(openlist)
                
                f=g[s_x+action[0]][s_y+action[1]]+heuristic((s_x+action[0],s_y+action[1]))
                heappush(openlist,(f,(s_x+action[0],s_y+action[1])))     
                
        
            
size=101
blocked=np.load('maze50.npy')
pyplot.figure(figsize=(10, 10))
pyplot.imshow(blocked, cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
search=np.zeros((size,size),dtype=int)
knownblocked=np.zeros((size,size),dtype=int)
nexpanded=0
g=np.empty((size,size),dtype=int)

start_x=np.random.randint(0,size-1)
start_y=np.random.randint(0,size-1)
target_x=np.random.randint(0,size-1)
target_y=np.random.randint(0,size-1)
while blocked[start_x][start_y]==1:
    print('start blocked,new start')
    start_x=np.random.randint(0,size-1)
    start_y=np.random.randint(0,size-1)
while blocked[target_x][target_y]==1:
    print('target blocked, new target')
    target_x=np.random.randint(0,size-1)
    target_y=np.random.randint(0,size-1)
fixedstart_x=start_x
fixedstart_y=start_y
print('start at',start_x,start_y)
print('target at',target_x,target_y)

g[start_x][start_y]=0
g[target_x][target_y]=MAX_INT

counter=0

closedlist=set()
openlist=[]
#heappush(openlist,(f,(start_x,start_y)))
validActions=actions((start_x,start_y))
tree={}
actionlist=actions((start_x,start_y))

while start_x!=target_x or start_y!=target_y:
    print('in main')
    current_x=start_x
    current_y=start_y
    counter=counter+1
    g[start_x][start_y]=0
    search[start_x][start_y]=counter
    g[target_x][target_y]=MAX_INT
    search[target_x][target_y]=counter
    closedlist=set()
    openlist=[]
    f=g[start_x][start_y]+heuristic((start_x,start_y))
    heappush(openlist,(f,(start_x,start_y)))
    ComputePath1()
    print('in main')
    if len(openlist)==0:
        print("cant reach target")
        sys.exit()
        break
    path=backtrace(tree,(start_x,start_y),(target_x,target_y))
    i=1
    print(path)
    while current_x!=target_x or current_y!=target_y  : #and len(actions(current_x,current_y))!=0:
        print("tracing",i)
        #follow tree from sstart to sgoal till the action becomes infinity cost i.e. blocked
        if blocked[path[i][0]][path[i][1]]==1:
            print('blocked at', path[i][0],path[i][1])
            knownblocked[path[i][0]][path[i][1]]=1
            break
        current_x=path[i][0]
        current_y=path[i][1]
        i=i+1
        print(current_x,current_y)
        #print(current_x!=target_x and current_y!=target_y and i<len(path))
    if(current_x!=start_x or current_y!=start_y):
        start_x=current_x
        start_y=current_y
    print('restart at',start_x,start_y)    
    #actionlist=actions(start_x,start_y)
 
print("Reached Target")
print("number of expanded nodes:",nexpanded )




    ##################################################################
 ########for lesser than tiebreaking   
    ##################################################################
    
search=np.zeros((size,size),dtype=int)
knownblocked=np.zeros((size,size),dtype=int)
nexpanded2=0
g=np.empty((size,size),dtype=int)

#start_x=np.random.randint(0,size-1)
#start_y=np.random.randint(0,size-1)
#target_x=np.random.randint(0,size-1)
#target_y=np.random.randint(0,size-1)
#while blocked[start_x][start_y]==1:
#    print('start blocked,new start')
#    start_x=np.random.randint(0,size-1)
#    start_y=np.random.randint(0,size-1)
#while blocked[target_x][target_y]==1:
#    print('target blocked, new target')
#    target_x=np.random.randint(0,size-1)
#    target_y=np.random.randint(0,size-1)
start_x=fixedstart_x
start_y=fixedstart_y
print('start at',start_x,start_y)
print('target at',target_x,target_y)

g[start_x][start_y]=0
g[target_x][target_y]=MAX_INT

counter=0

closedlist=set()
openlist=[]
#heappush(openlist,(f,(start_x,start_y)))
validActions=actions((start_x,start_y))
tree={}
actionlist=actions((start_x,start_y))

while start_x!=target_x or start_y!=target_y:
    print('in main')
    current_x=start_x
    current_y=start_y
    counter=counter+1
    g[start_x][start_y]=0
    search[start_x][start_y]=counter
    g[target_x][target_y]=MAX_INT
    search[target_x][target_y]=counter
    closedlist=set()
    openlist=[]
    f=g[start_x][start_y]+heuristic((start_x,start_y))
    heappush(openlist,(f,(start_x,start_y)))
    ComputePath2()
    print('in main')
    if len(openlist)==0:
        print("cant reach target")
        sys.exit()
        break
    path=backtrace(tree,(start_x,start_y),(target_x,target_y))
    i=1
    print(path)
    while current_x!=target_x or current_y!=target_y  : #and len(actions(current_x,current_y))!=0:
        print("tracing",i)
        #follow tree from sstart to sgoal till the action becomes infinity cost i.e. blocked
        if blocked[path[i][0]][path[i][1]]==1:
            print('blocked at', path[i][0],path[i][1])
            knownblocked[path[i][0]][path[i][1]]=1
            break
        current_x=path[i][0]
        current_y=path[i][1]
        i=i+1
        print(current_x,current_y)
        #print(current_x!=target_x and current_y!=target_y and i<len(path))
    if(current_x!=start_x or current_y!=start_y):
        start_x=current_x
        start_y=current_y
    print('restart at',start_x,start_y)    
    #actionlist=actions(start_x,start_y)
 
print("Reached Target")
print("number of expanded nodes:",nexpanded2 )
    
file= open("comparePriority.txt","a") 
#file.write("mazeno\tGgreater\tGlesser\n")
file.write("%d\t%d\t%d\n" % (50,nexpanded,nexpanded2))  
file.close()   
    
    
    
    
    
    
    
    
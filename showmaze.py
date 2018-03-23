#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:11:52 2018

@author: shubhamsinha
"""

import numpy as np
import math
from heapq import *
import sys
import matplotlib.pyplot as pyplot

z=4
maze='maze'+str(z)+'.npy'
blocked=np.load(maze)
pyplot.figure(figsize=(10, 10))
pyplot.imshow(blocked, cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()

#zeroes=0
#tot=0
#for i in range(0,101):
#    for j in range(0,101):
#        if blocked[i][j]==0:
#            zeroes+=1
#        tot+=1
#
#print('zeroes',zeroes)
#print("tot",tot)
#
#zeroes=0
#tot=0
#for i in range(0,101):
#    for j in range(0,101):
#        if g[i][j]!=0:
#            zeroes+=1
#        tot+=1
#!/usr/bin/env python3

import sys
import numpy as np

def read_input(file): 
    for line in file:
        yield line.strip()
input = read_input(sys.stdin) # Read each row of data sequentially

def lm_row(datairow):
    datairow = ["1"]+datairow.split(",") #add beta0
    datairow = np.array(datairow,float)
    y = datairow[len(datairow)-1]
    x =  datairow[:(len(datairow)-1)]
    xy = x*y
    xx = np.matrix(x).T*np.matrix(x)
    return xy,xx

res = map(lm_row,input) # in py3, result of map is generator

p = 0
for r in res: # go through the generator
    xy_tmp,xx_tmp = r
    if p==0: # initialize the xx and xy
        p = len(xy_tmp)
        xx = np.diag(np.zeros(p)) # all 0 array(matrix)
        xy = np.zeros(p)
    xx += xx_tmp
    xy += xy_tmp

xy = list(xy)
xx = xx.reshape(1,p**2)
xx = list(xx[0]) # get the xx in one time

data = xy + xx

print("\t".join(str(i) for i in data))
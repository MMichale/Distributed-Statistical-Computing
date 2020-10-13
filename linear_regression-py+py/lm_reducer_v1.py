#!/usr/bin/env python3

import sys 
import numpy as np

def read_input(file):
    for line in file:
        yield line.strip()
input = read_input(sys.stdin) 

def forsumup(datairow):
    datairow = datairow.split("\t")
    datairow = np.array(datairow,float)
    return datairow

vecsumup = np.array(list(map(forsumup,input))) # np.array receive list
sumup = np.sum(vecsumup,axis = 0) # sum by row, so the shape of sumup should be p**2+p

p = int((-1+np.sqrt(1+4.0*len(sumup)))/2.0) # solve a quadratic system of equations
XY = np.mat(sumup[:p]).T # xy is a column vector
XX = np.mat(sumup[p:].reshape(p,p)).I
beta = XX*XY
print(beta)
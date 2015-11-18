# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:45:27 2015

@author: splatt
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def W(x):
    return (3.5*np.exp((-((x-3)**2))/3.)+2.*np.exp((-((x+1.5)**2))/0.5))/13.25155870806912

N=100000
n=100
x=np.linspace(-5,10,N)
x[0]=1.
L=[]
for j in range(0,n):   
    np.random.seed(j*2)
    r = np.random.uniform(low=0.0, high=1.0, size=N)
    np.random.seed(j*2+1)
    r2 = np.random.uniform(low=-1.0, high=1.0, size=N)
    for i in range(0, N-1): 
        x_p= x[i]+4.*r2[i]
        if  W(x_p)/W(x[i])> r[i]:
            x[i+1] = x_p
        else:
            x[i+1] = x[i]
    L.append(np.histogram(x,bins=50,normed=True))
    
menStd=np.zeros(50)
for l in range(0,50):
    de=np.zeros(50)
    for k in range(0,50):
        y,binEdges=L[k]
        de[k]=y[l]
    menStd[l]=np.std(de)
print menStd

plt.clf()    
y,binEdges=np.histogram(x,bins=50, normed=True)
bincenters =2.8*(binEdges[1:]+binEdges[:-1])
plt.bar(bincenters,y, color='r', yerr=menStd)
plt.xlabel('x')
plt.ylabel('W(x)')
red_patch = mpatches.Patch(color='red', label='Histograma')
plt.legend(handles=[red_patch])
plt.show()
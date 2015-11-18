# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:38:47 2015

@author: splatt
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def W(x):
    return (3.5*np.exp((-((x-3)**2))/3.)+2.*np.exp((-((x+1.5)**2))/0.5))/13.25155870806912
    
N=100000
np.random.seed(50)
x=np.linspace(-5,10,N)
plt.clf()
plt.plot(x,W(x))
x[0]=1.
r = np.random.uniform(low=0.0, high=1.0, size=N)
np.random.seed(51)
r2 = np.random.uniform(low=-1.0, high=1.0, size=N)
contador=0
for i in range(0, N-1): 
    x_p= x[i]+4.*r2[i]
    if  W(x_p)/W(x[i])> r[i]:
        x[i+1] = x_p
        contador+=1
    else:
        x[i+1] = x[i]
print("acepta un ", contador*100/float(N))," %"
plt.hist(x, bins=50, normed=True, color='red')
red_patch = mpatches.Patch(color='red', label='Histograma')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=10.,label='W(x)')
plt.legend(handles=[red_patch])
plt.xlabel('x')
plt.ylabel('W(x)')
plt.show()
plt.draw()
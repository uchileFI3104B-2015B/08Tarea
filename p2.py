''' muestra aleatoria'''
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

def w(x):
    '''distribucion normalizada'''
    a= 3.5* np.exp((-(x-3)**2 )/3) + 2* np.exp((-(x-1.5)**2 )/0.5)
    pn= 13.171317181206 #para normalizar (integral)
    normalizada= a/pn
    return normalizada

def metropolis(x,r):
    '''algoritmo metropolis'''
    xn= xp + r* np.random.uniform(-1,1)
    if w(xn) / w(xp) > r:
        xp=xn
    return xp

#condiciones
r=3
n=1000000
x=np.linspace(-10,10,n)
xp=np.zeros(n)
xp[0]=np.random.uniform(-10,10)

f=plt.figure()
f.clf()
ax=f.add_subplot
hist, bins = plt.hist(xp, bins=50, normed=True)
ax.plot(x,w(x))
ax.set_xlabel()
ax.set_ylabel()
plt.draw()
plt.show()

plt.savefig(a)

'''encontrando centro de masa'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

n=1000000
posx=0.0
posy=0.0
posz=0.0
m=0.0
vol=2.0*8.0*2.0
for i in range(1, n):
    x= 1+2*np.random.uniform(0.,1.)
    y= (-4)+8*np.random.uniform(0.,1.)
    z= (-1)+2*np.random.uniform(0.,1.)
    ro=0.5*(x**2 + y**2 + z**2)
    toro= z**2 + (np.sqrt((x**2)+(y**2)) -3)**2
    cilindro= (x-2)**2 + z**2
    if (toro <=1 and cilindro <=1):
        m+= ro
        posx += x*ro
        posy += y*ro
        posz += z*ro

mm=vol*m
x=vol* posx /(n*mm)
y=vol* posy /(n*mm)
z=vol* posz /(n*mm)

cm=x,y,z
print cm

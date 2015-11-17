	#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from __future__ import division
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
'''
este script utiliza el algoritmo de Metrópolis
para obtener una muestra  aleatoria de numeros
con cierta distribucion dada.
'''


puntos=[]
n=1000000
#w=3.5*exp((-(x-3)^2)/3.) + 2 exp((-(x+1.5)^2/(0.5)
np.random.seed(19)
xn=-1+2*np.random.sample()

print xn
d=2
for i in range(n):
    r=-1+2*np.random.sample()
    xp = xn + (d*r)

    wxp=3.5*np.exp((-(xp-3)**2)/3.) + 2*np.exp(-((xp+1.5)**2)/0.5)
    wxn=3.5*np.exp((-(xn-3)**2)/3.) + 2*np.exp(-((xn+1.5)**2)/0.5)
    if (wxp / wxn) > np.random.sample(): #problema con positivos

        xn_plus=xp
        puntos.append(xn_plus)
    else:
        xn_plus=xn


    xn=xn_plus
print len(puntos)/n #puntos



num_bins = 200
# histograma
n, bins, patches = plt.hist(puntos, num_bins, normed=1, facecolor='green', alpha=0.5)

plt.xlabel('x')
plt.ylabel('w')
plt.title(r'Histograma')


plt.subplots_adjust(left=0.15)
plt.show()

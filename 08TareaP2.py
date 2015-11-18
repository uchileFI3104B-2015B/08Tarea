#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from __future__ import division
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
'''
este script utiliza el algoritmo de Metrópolis
para obtener una muestra  aleatoria de numeros
con la distribucion :
w=3.5*exp((-(x-3)**2)/3.) + 2 exp((-(x+1.5)**2)/0.5)
'''


def MetropolisP2(n, d, xn):
    for i in range(n):
        r = -1+2*np.random.sample()
        xp = xn + (d*r)
        wxp = 3.5*np.exp((-(xp-3)**2)/3.) + 2*np.exp((-(xp+1.5)**2)/0.5)
        wxn = 3.5*np.exp((-(xn-3)**2)/3.) + 2*np.exp((-(xn+1.5)**2)/0.5)
        if (wxp/wxn) > np.random.sample():
            xn_plus = xp
            puntos.append(xn_plus)
        else:
            xn_plus = xn
            puntos.append(xn_plus)
        xn = xn_plus

# main
# setup

puntos = []
n = 10000000
np.random.seed(19)  # semilla
xn = -1+2*np.random.sample()  # valor inicial, depende de la semilla
d = 4
MetropolisP2(n, d, xn)

# Plot Histograma

integral = np.sqrt(np.pi)*(3.5*np.sqrt(3)+2*np.sqrt(0.5))
num_bins = 100
n, bins, patches = plt.hist(puntos,
                            num_bins, normed=True, facecolor='green')
x = np.linspace(bins[0], bins[-1], 10000)
w = 3.5*np.exp((-(x-3)**2)/3.) + 2*np.exp((-(x+1.5)**2)/0.5)
plt.figure(1)
plt.plot(x, w/integral, 'r', label='Distribucion W(x)')
plt.xlabel('x')
plt.ylabel('w(x)')
plt.title('Histograma')
plt.legend()
plt.savefig('Histograma.jpg')
plt.show()

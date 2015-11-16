#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(0)
# funciones estructurales

def w(x):
    '''
    distribucion sin normalizar
    '''
    w = 3.5 * np.exp(- (x - 3) ** 2 / 3) + 2 * np.exp(- (x + 1.5) ** 2 / 0.5)
    return w
    pass


def normalizar():
    '''
    valor de la integral de la distribucion en todo el espacio
    se propone el calculo numerico, pero por ahora se usa un valor dado por la
    solucion en wolframalpha de
    3.5 * exp(- (x - 3) ** 2 / 3) + 2 * exp(- (x + 1.5) ** 2 / 0.5)
    '''
    return 13.2516
    pass


def W(x):
    '''
    distribucion normalizada
    '''
    return w(x) / normalizar()
    pass


def cond_metropolis(xn, d):
    '''
    aplica condicion de metropolis
    '''
    xp = xn + d * np.random.uniform(- 1, 1)
    if W(xp) / W(xn) > np.random.uniform(- 1, 1):
        xn = xp
    return xn
    pass


def es_optimo(di, n):
    '''
    busca el paso optimo
    '''
    xn = np.zeros(n)
    xn[0] = np.random.uniform(- 8, 8)
    c = 0
    for i in range(1, n):
        xn[i] = cond_metropolis(xn[i-1], d)
        if xn[i] == xn[i-1]:
            c += 1
    print c
    print n
    return c >= n / 2
    pass


# inicializacion
n = 100000
d = 0.1
x = np.linspace(-8, 8, n)
xn = np.zeros(n)
xn[0] = np.random.uniform(- 8, 8)
print es_optimo(d, n)
for i in range(1, n):
    xn[i] = cond_metropolis(xn[i-1], d)
# iteracion

# plots
fig=plt.figure()
fig.clf()
ax1=fig.add_subplot(111)
ax1.plot(x, w(x))
plt.draw()
plt.show()

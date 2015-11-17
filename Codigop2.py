
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
# funciones estructurales

def w(x):
    '''
    distribucion sin normalizar
    '''
    w = 3.5 * np.exp(- (x - 3) ** 2 / 3.) + 2 * np.exp(- (x + 1.5) ** 2 / 0.5)
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
    if W(xp) / W(xn) > np.random.uniform(0 , 1):
        xn = xp
    return xn
    pass


def es_optimo(d_in, n):
    '''
    busca el paso optimo
    '''
    xn = np.zeros(n)
    xn[0] = np.random.uniform(- 8, 8)
    c = 0
    for i in range(1, n):
        xn[i] = cond_metropolis(xn[i-1], d_in)
        if xn[i] == xn[i-1]:
            c += 1
    return c >= n / 2
    pass



# iteracion
n = 1000
s = np.linspace(1, 10, 10)
xi = np.linspace(-4, 5, 10)
#W_i = np.zeros((len(s), n))
w_hist = np.zeros((len(s), 100))
W_mean = np.zeros(100)
W_std = np.zeros(100)
for i in range(1, len(s)):
    s_i = s[i]
    x_i = xi[i]
    b = np.histogram(calcula_dist(n, s_i, x_i), bins=100, range=(-8, 8), normed=True)
    w_hist[i-1] = b[0]
for l in range(1, 100):
    a = np.zeros(len(s))
    for m in range(1, len(s)):
        a[m-1] = w_hist[m-1, l-1]
    W_mean[l-1] = np.mean(a)
    W_std[l-1] = np.std(a)
# plots
fig=plt.figure()
fig.clf()
ax1=fig.add_subplot(111)
n, bins, patches = ax1.hist(xn, 100, normed=True)
ax1.plot(x, W(x))
ax1.set_xlabel("X")
ax1.set_ylabel("W(x)")
plt.draw()
plt.show()

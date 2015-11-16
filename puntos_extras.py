#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

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


def calcula_dist(n, s, xi):
    s = np.int(s)
    np.random.seed(s)
    n_p = 10000
    x = np.linspace(-8, 8, n)
    xn = np.zeros(n)
    xn[0] = np.random.uniform(- 8, 8)
    for i in range(1, 10):
        if es_optimo(i, n_p):
            d = i
            break
    for i in range(1, n):
        xn[i] = cond_metropolis(xn[i-1], d)
    return xn[i]


# iteracion
n = 1000
s = np.linspace(1, 10, 10)
xi = np.linspace(-4, 5, 10)
X = np.zeros(len(s))
print s
for i in range(1, 10):
    X[i-1] = calcula_dist(n, s[i], xi[i])

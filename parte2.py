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
    if W(xp) / W(xn) > np.random.uniform(0, 1):
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


# inicializacion
n = 10000000  # diez millones de puntos
n_p = 10000  # n de prueba para buscar d optimo
x = np.linspace(-8, 8, n)  # aqui se concentra la mayor parte de la dist
xn = np.zeros(n)
xn[0] = np.random.uniform(- 8, 8)
# iteracion
for i in range(1, 10):
    '''
    Se busca un d optimo de forma bastante simple. se podria avanzar en un paso
    mas pequeño para lograr un valor mas preciso termina con el primer valor
    que acepta al menos el 50 porciento de los datos
    '''
    if es_optimo(i, n_p):
        d = i
        print d
        break
for i in range(1, n):
    xn[i] = cond_metropolis(xn[i-1], d)
# plots
fig = plt.figure()
fig.clf()
ax1 = fig.add_subplot(111)
n, bins, patches = ax1.hist(xn, 100, normed=True)
ax1.plot(x, W(x))
ax1.set_xlabel("X")
ax1.set_ylabel("W(x)")
plt.savefig("parte2.png")
plt.draw()
plt.show()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def distribucion(x):
    w = (3.5 * np.exp(- (x - 3.)**2 / 3.) +
         2 * np.exp(- (x + 1.5)**2 / 0.5))
    return w


def normalizacion(f, a=-100, b=100):
    '''
    Función que busca el factor normalizador de una función.
    '''
    N = integrate.quad(f, a, b)
    return N[0]


def dist_normalizada(x):
    wn = distribucion(x) / normalizacion(distribucion)
    return wn


def avanza_metropolis(xn, delta):
    r = np.random.uniform(-1, 1)
    xp = xn + delta * r
    # Si se cumple la condición, entonces avanzamos delta.
    # De lo contrario, nos quedamos en el mismo punto.
    if distribucion(xp) / distribucion(xn) > np.random.uniform(0., 1.):
        return xp
    else:
        return xn


def mejor_delta(N, dmin, dmax):
    '''
    Para el algoritmo de Metrópolis se busca que, almenos el 50%
    de los puntos sean aceptados, por lo que necesitamos encontrar
    el factor "d" que logre dicho objetivo.
    '''
    D = np.linspace(dmin, dmax, N)
    puntos = np.zeros(N)

    porcentaje = 0
    j = 0
    while np.fabs(porcentaje - 50.) >= 0.005:
        aceptados = 0
        puntos[0] = np.random.uniform(-10., 10.)
        for i in range(1, N):
            puntos[i] = avanza_metropolis(puntos[i-1], D[j])
            if puntos[i] == puntos[i-1]:
                aceptados += 1

        porcentaje = 100 * aceptados / N
        j += 1

    return D[j]


# Setup

np.random.seed(123)
n = 10000000

delta = mejor_delta(1000, -20, 20)

x = np.zeros(n)
w = np.zeros(n)
x[0] = np.random.uniform(-5, 15)
w[0] = dist_normalizada(x[0])

for i in range(1, n):
    x[i] = avanza_metropolis(x[i-1], delta)
    w[i] = dist_normalizada(x[1])

x_distribucion = np.linspace(-10, 10, n)

fig = plt.figure(1)
fig.clf()

ax = fig.add_subplot(111)
n, bins, patches = ax.hist(x, 100, normed=True, color='blue')
ax.plot(x_distribucion, dist_normalizada(x_distribucion),
        color='green', linewidth=2)
ax.set_xlabel("x")
ax.set_ylabel("Distribución: W(x)")

plt.savefig('histograma.png')

plt.draw()
plt.show()

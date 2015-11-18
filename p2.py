#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Aquí va el docstring de mi codigo explicando que cosas hace
'''
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def w_sin_normalizar(x):
    '''docstring'''
    return 3.5 * np.exp(-(x-3)**2 / 3) + 2 * np.exp(-(x+1.5)**2 / 0.5)


def normalizador(funcion, rango=[-100, 100]):
    '''Bla'''
    integral = scipy.integrate.quad(funcion, rango[0], rango[1])
    return integral[0]


def w(x):
    return w_sin_normalizar(x) / normalizador(w_sin_normalizar)


def un_paso_metropolis(xn, delta):
    '''Docstring de esta funcion'''
    r = np.random.uniform(-1, 1)
    xp = xn + delta * r

    # Criterio de Metrópolis:
    if w_sin_normalizar(xp) / w_sin_normalizar(xn) > np.random.uniform(0, 1):
        return xp
    else:
        return xn


def calcular_optimizac_delta(N, delta):
    '''Calcula que tan optimo es un delta dado, pues se busca cierto delta para
    cuando se aceptan aprximadamente la mitad de las proposiciones'''
    x = np.zeros(N)
    aceptados = 0
    total = N
    for i in range(1, N):
        x[i] = un_paso_metropolis(x[i], delta)
        if x[i] != x[i-1]:
            aceptados += 1

    # Cuando encuentre cierto delta tal que esta funcion me
    # retorne 0.5, va a ser el delta optimo :)
    porcentaje = aceptados / total
    return porcentaje >= 0.5


# Main
np.random.seed(1)
N_metropolis = 1000000

# Encontrar delta optimo
'''
N_pasos_delta =  100   # Pasos para encontrar el delta optimo
set_deltas = np.linspace(1, 21, N_pasos_delta)
for i in range(N_pasos_delta):
    d = set_deltas[i]
    if calcular_optimizac_delta(N_metropolis, d):
        delta = d
        print d
        break
'''

x = np.zeros(N_metropolis)
dist = np.zeros(N_metropolis)
x[0] = np.random.uniform(-6, 10)
dist[0] = w(x[0])
for i in range(1, N_metropolis):
    x[i] = un_paso_metropolis(x[i-1], 14)
    dist[i] = w(x[1])

x_dist = np.linspace(-10, 10, N_metropolis)

fig = plt.figure(1)
fig.clf()
ax1 = fig.add_subplot(111)
n, bins, patches = ax1.hist(x, 50, normed=True, color='red')
ax1.plot(x_dist, w(x_dist), color='blue', linewidth=2)
ax1.set_xlabel("X")
ax1.set_ylabel("W(x)")
plt.savefig('histograma.eps')
plt.draw()
plt.show()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(564)  # Mi rank en la competencia de pokemon shuffle


def W(x):
    '''
    Distribucion no normalizada de la cual se extraeran numeros
    '''
    return 3.5 * np.exp(-(x-3.)**2. / 3.) + 2. * np.exp(-2. * (x + 1.5)**2.)


def normalizar(x):
    return W(x) / norma


def metropolis(xn, delta):
    xp = xn + delta * np.random.uniform(low=-1, high=1)
    if W(xp) / W(xn) > np.random.uniform(0, 1):  # criterio
        xn = xp
    return xn


def delta_finder(xn, N, d):
    xn_1 = np.zeros(N)
    xn_1[0] = xn
    recha = 0.
    for i in range(len(xn_1) - 1):
        xn_1[i+1] = metropolis(xn_1[i], d)
        if xn_1[i+1] == xn_1[i]:
            recha += 1.
    porcentaje = (N - recha) / N
    return porcentaje, xn_1


# Main
x = np.linspace(-10, 10, 1000)
norma = np.trapz(W(x), x)

N = 100
n = 50
xn_0 = 0
deltas = np.linspace(1., 10., n)
porcentaje = np.zeros(n)

for i in range(n):
    porcentajes, xn_1 = delta_finder(xn_0, N, deltas[i])
    porcentaje[i] = np.copy(porcentajes)

for i in range(n):
    if np.fabs(porcentaje[i]-0.5) <= 0.01:  # se pide precisión del 1%
        d = deltas[i]

# Plots
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111)
plt.plot(x, normalizar(x), color='r', label="Distribucion teorica")
ax.set_xlabel("x")
ax.set_ylabel("W(x)")

percent_hist, xn_1_hist = delta_finder(xn_0, 10**7, d)
n, bins, patches = plt.hist(xn_1_hist, bins=100, normed=1)

plt.legend(loc=2)
plt.savefig('W_x7.png')
plt.show()
plt.draw()

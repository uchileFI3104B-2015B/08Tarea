#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(347)
DELTA = 4
N_puntos = 10000000

def W(x):
    exp1 = 3.5 * np.exp(-(np.power(x - 3, 2))/3)
    exp2 = 2 * np.exp(-(np.power(x + 1.5, 2))/0.5)
    return exp1 + exp2

def proposicion(xn):
    r = np.random.uniform(low=-1, high=1)
    return xn + r*DELTA

X = np.zeros(N_puntos + 1)
n_aceptados = 0
n = 0
while n < N_puntos:
    s = np.random.uniform(low=0, high=1)
    xP = proposicion(X[n])
    if W(xP) / W(X[n]) > s:
        X[n+1] = xP
        n_aceptados += 1
    else:
        X[n+1] = X[n]
    n += 1

x_w = np.linspace(-4, 8, 10000)
I = np.sqrt(np.pi) * (3.5*np.sqrt(3) + 2*np.sqrt(0.5))
print "Numero de proposiciones aceptadas: ", n_aceptados

plt.clf()
plt.figure(1)
plt.hist(X, bins=100, normed=True)
plt.plot(x_w, W(x_w)/I, color='r', linewidth=2)
plt.show()

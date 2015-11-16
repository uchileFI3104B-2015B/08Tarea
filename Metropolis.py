#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este script genera una distribución de números aleatorios dada la función W(x)
definida en el primer método, usando el algoritmo de Metropolis. Imprime el
número de proposiciones aceptadas para valores de x y genera un gráfico con la
distribución obtenida y la deseada, ambas normalizadas.
'''

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

x_w = np.linspace(-5, 10, 10000)
I = np.sqrt(np.pi) * (3.5*np.sqrt(3) + 2*np.sqrt(0.5))
print "Numero de proposiciones aceptadas: ", n_aceptados

plt.clf()
plt.figure(1)
plt.hist(X, bins=100, range=[-5, 10], normed=True, label="Histograma")
plt.plot(x_w, W(x_w)/I, color='r', linewidth=2, label="Distribucion deseada")
plt.ylim([0, 0.32])
plt.xlim([-5, 10])
plt.title('Distribucion W(x) deseada y generada via Metropolis')
plt.xlabel('x')
plt.legend()
plt.savefig('Metropolis.eps')
plt.show()

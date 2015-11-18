#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pdb

'''Script que obtiene una muestra aleatoria de n?meros con la distibuci?n:
W(x) = 3.5 * np.exp(-(x - 3) ** 2 / 3) + 2 * np.exp(-(x + 1.5) ** 2 / 0.5)
utilizando el algoritmo de metr?polis'''


def W(x):
    '''distribuci?n de probabilidad que usaremos (normalizada)'''
    w = 3.5 * np.exp(-(x - 3) ** 2 / 3) + 2 * np.exp(-(x + 1.5) ** 2 / 0.5)
    a1 = 3.5 * np.sqrt(3 * np.pi)
    a2 = 2 * np.sqrt(1/2 * np.pi)
    return w / (a1 + a2)


def llenar_errores(HIST):
    ''' recibe la matriz con los valores para cada histograma para Nmc
    repeticiones y devuelve un arreglo con la desviacion estandar
    de cada bin'''
    N = HIST.shape[1]
    error = np.zeros(N)
    for i in range(N):
        bin_1 = HIST[:, i]
        error[i] = np.std(bin_1)
    return error

HIST = np.zeros((100, 50))  # matrices donde se
EDGES = np.zeros((100, 51))  # guardaran los histogramas para cada iteracion
ERRORES = np.zeros(50)  # matriz donde se guardaran los errores de cada bin
SEMILLA = np.linspace(1, 100, 100)

for j in range(len(SEMILLA)):
    print(j)
    np.random.seed(int(SEMILLA[j]))
    DELTA = 10
    x_n = np.random.uniform()
    p_n = W(x_n)
    N = 100000
    muestra = np.zeros(N)
    for i in range(N):
        x_n1 = x_n + DELTA * np.random.uniform(-1, 1)
        p_n1 = W(x_n1)
        a = p_n1 / p_n
        if a >= 1:
            muestra[i] = x_n1
            x_n = x_n1
            p_n = p_n1
        else:
            u = np.random.uniform()
            if u < a:
                muestra[i] = x_n1
                x_n = x_n1
                p_n = p_n1
            else:
                muestra[i] = x_n

    hist, bin_edges = np.histogram(muestra, bins=50, density=True)
    HIST[j, :] = hist.copy()
    EDGES[j, :] = bin_edges.copy()
    print("fin")
ERRORES = llenar_errores(HIST)
bincenters = 0.5*(EDGES[1, :][1:]+EDGES[1, :][:-1])
width = 0.2
plt.bar(bincenters, HIST[1, :], width=width, color='g',
        yerr=ERRORES, label="Muestra obtenida")


x = np.linspace(-100, 100, 1000)
plt.xlim(-4, 8)
w = np.vectorize(W)
distr = w(x)
plt.plot(x, distr, color="red", label="distribucion esperada")
plt.title("Muestra obtenida y distribucion esperada")
plt.ylabel("Probabilidad")
plt.xlabel("X")
plt.legend()
plt.savefig("errores.jpg")
plt.show()

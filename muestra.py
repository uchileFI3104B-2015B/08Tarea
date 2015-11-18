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


def mostrar(muestra):
    ''' plot de un histograma de la muestra obtenida y la distribuci?n
    normalizada esperada'''
    fig, ax = plt.subplots()
    x = np.linspace(-100, 100, 1000)
    w = np.vectorize(W)
    distr = w(x)
    num_bins = 50
    n, bins, patches = ax.hist(muestra, num_bins, normed=True,
                               facecolor='green',
                               alpha=0.5, label="muestra")
    ax.set_xlim(-4, 8)
    ax.plot(x, distr, color="red", label="distribucion esperada")
    ax.set_title("Muestra obtenida y distribucion esperada")
    ax.set_ylabel("Probabilidad")
    ax.set_xlabel("X")
    plt.legend()
    plt.savefig("histograma.jpg")
    plt.show()


SEMILLA = 3
np.random.seed(int(SEMILLA))
DELTA = 10

x_n = np.random.uniform()
p_n = W(x_n)
N = 10000000
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

mostrar(muestra)

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
    return xn


def ultimate_function(n, s, xi):
    '''
    no se me ocurrio otro nombre por ahora, ya que es la funcion que agrupa
    (casi) todo.
    agrupa los datos como histograma para repeticiones de len(s). con s setea
    la semilla, xi corresponde al punto de partida del algoritmo. realiza la
    iteracion para cada s, xi (con la misma dimension).
    finalmente, calcula el promedio de la distribucion para cada bin del
    histograma. regresa los promedios y desviacion estandar de los valores para
    los bins.
    '''
    w_hist = np.zeros((len(s), 100))
    W_mean = np.zeros(100)
    W_std = np.zeros(100)
    for i in range(1, len(s)):
        print i
        s_i = s[i]
        x_i = xi[i]
        b = np.histogram(calcula_dist(n, s_i, x_i), bins=100,
                         range=(-8, 8), normed=True)
        w_hist[i-1] = b[0]
    for l in range(1, 100):
        a = np.zeros(len(s))
        for m in range(1, len(s)):
            a[m-1] = w_hist[m-1, l-1]
        W_mean[l-1] = np.mean(a)
        W_std[l-1] = np.std(a)
    return W_mean, W_std, b[1]


# iteracion
n = 10000000
s = np.linspace(1, 100, 100)
xi = np.linspace(-4, 5, 100)
w, s, x_hist = ultimate_function(n, s, xi)

# plots
'''
fig, ax = plt.subplots()
f = plt.bar(np.arrange(100), W_mean, 0.16, )
'''
fig = plt.figure()
fig.clf()
ax1 = fig.add_subplot(111)
x_hist = x_hist[1:]
x = np.linspace(-8, 8, 100)
ax1.bar(x_hist, w, align='center', width=0.16, label="Distrubucion Obtenida")
ax1.errorbar(x + 0.08, w, yerr=s, fmt='.', color='r', label="Error")
ax1.set_xlabel("X")
ax1.set_ylabel("W(x)")
plt.legend()
plt.savefig("histograma_con_errorbar.png")
plt.draw()
plt.show()

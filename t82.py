#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''utilizando el algoritmo de metropolis  Se desea obtener una muestra
aleatoria de números con la distribución
(no normalizada) w(x)'''

import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt

np.random.seed(121)  # se fija semilla


def fn_de_peso(x):
    ''' se define la funcion w(x) la cual es la
    distribución '''
    return (3.5 * np.exp(-((x - 3)**2) / 3) +
            2 * np.exp(-((x + 1.5)**2)/0.5))

a = -100
b = 100
'''calculo de la integral para normalizar'''
integral = si.quad(fn_de_peso, a, b)
inte = integral[0]


def fn_normalizada(x):
    '''se normaliza la fn a traves de
    la división de su integral'''
    norma = fn_de_peso(x) / inte
    return norma

calculo = si.quad(fn_normalizada, a, b)
print 'valor integral',
print calculo[0]


def metropolis(delta, xn):
    ''' se define la funcion de la metropolis que recive del y xn
    en donde la gracia es ver los xp'''

    xp = xn + delta * np.random.uniform(-1, 1)
    if fn_normalizada(xp) / fn_normalizada(xn) > np.random.uniform(0, 1):
        xn = xp
    return xn
    pass


def optimo(delta1, n):
    ''' se verifica si x_p es optimo osea si es al menos un 50 porciento
    de los casos '''
    xn = np.zeros(n)
    xn[0] = np.random.uniform(-8, 8)
    contador = 0.0
    for i in range(1, n):
        xn[i] = metropolis(delta1, xn[i-1])
        if xn[i] == xn[i-1]:
            contador += 1
    return contador >= n / 2
    pass

delta1 = delta = 4.1
n = 10000000
xn = np.zeros(n)
xn[0] = np.random.uniform(-6, 6)
a = optimo(delta1, n)
print 'porcentaje',
print a
x = np.linspace(-6, 6, n)
for i in range(1, n):
    xn[i] = metropolis(delta, xn[i-1])
# plots
fig = plt.figure()
fig.clf()
ax1 = fig.add_subplot(111)
n, bins, patches = ax1.hist(xn, 100, normed=True)
ax1.plot(x, fn_normalizada(x))
ax1.set_xlabel('$X$', fontsize=10)
ax1.set_ylabel('$W(x)$', fontsize=10)
ax1.set_title('$\ Funcion \ de \ Distribucion $', fontsize=10)
plt.savefig("histograma.png")
plt.draw()
plt.show()

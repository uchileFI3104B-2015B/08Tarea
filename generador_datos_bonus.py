'''
Este script genera los datos a utilizar en el script bonus.py.
Los datos corresponden al valor asociado a cada bin (50 bins desde -10 a 10)
del histograma de la muestra (de 10 millones de puntos) que se obtiene al
realizar cada una de las 101 repeticiones del algoritmo de metrópolis. Con
delta = 3.79.
'''
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapz
import time
start_time = time.time()


def w(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion


def w_normalizado(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion / integral


def avanza_metropolis(w_normalizado, xn, delta):
    r = np.random.uniform(-1., 1.)
    xp = xn + delta * r
    gamma = np.random.uniform(0., 1.)
    if w(xp) / w(xn) > gamma:
        return xp
    else:
        return xn


def xn_mas_1(w, xn, N, delta):
    xn_mas_1 = np.zeros(N)
    xn_mas_1[0] = np.copy(xn)
    for i in range(len(xn_mas_1)-1):
        xn_mas_1[i+1] = avanza_metropolis(w_normalizado, xn_mas_1[i], delta)
    return xn_mas_1

# Se escoge semilla
np.random.seed(212)
datos_n = np.empty(0)
d = 3.79
xn = np.linspace(-10, 10, 101)
bins_escogido = np.linspace(-10, 10, 51)
n = np.zeros(len(xn), dtype=object)
bins = np.zeros(len(xn), dtype=object)
f_distribucion_w = np.zeros(len(xn), dtype=object)
for i in range(len(xn)):
    f_distribucion_w[i] = xn_mas_1(w, xn[i], 10**7, 3.79)
    n[i], bins, patches = plt.hist(f_distribucion_w[i], bins_escogido,
                                   normed=1, facecolor='g', alpha=0.5)
    datos_n = np.append(datos_n, n[i])

np.savetxt('datos_10_millones_puntos.txt', datos_n)

print("--- %s seconds ---" % (time.time() - start_time))

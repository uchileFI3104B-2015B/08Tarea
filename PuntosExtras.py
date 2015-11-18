#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from __future__ import division
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

'''
este script utiliza el algoritmo de Metrópolis
100 veces para determinar la incertidumbre asociada
a cada bin del histograma para graficar el histograma
con barras de error
'''


def MetropolisP2(n, d, xn):
    '''
    Funcion que toma el numero de la muestra, el valor fijo d
     y el punto inicial xn para calcular los datos del histograma
    '''
    for i in range(n):
        r = -1+2*np.random.sample()
        xp = xn + (d*r)
        wxp = 3.5*np.exp((-(xp-3)**2)/3.) + 2*np.exp((-(xp+1.5)**2)/0.5)
        wxn = 3.5*np.exp((-(xn-3)**2)/3.) + 2*np.exp((-(xn+1.5)**2)/0.5)
        if (wxp/wxn) > np.random.sample():
            xn_plus = xp
            puntos.append(xn_plus)
        else:
            xn_plus = xn
            puntos.append(xn_plus)
        xn = xn_plus

# main
# setup

puntos = []
numero_muestra = 1000000
d = 2
integral = np.sqrt(np.pi)*(3.5*np.sqrt(3)+2*np.sqrt(0.5))
num_bins = 100
Lista_bins = []
Lista_n = []
n_mean_stds = []
n_mean = []
n_std = []
for i in range(100):
    puntos = []
    np.random.seed(1+i)
    xn = -1+2*np.random.sample()
    MetropolisP2(numero_muestra, d, xn)
    n, bins, patches = plt.hist(puntos,
                                num_bins, normed=True, facecolor='green')
    Lista_n.append(n)
Lista_bins.append(bins)

for i in range(100):  # ordenar los numeros para el promedio y la desviacion
    auxiliar = []
    for j in range(100):
        auxiliar.append(Lista_n[j][i])
    n_mean_stds.append(auxiliar)


for i in range(100):
    n_mean.append(np.mean(n_mean_stds[i]))
    n_std.append(np.std(n_mean_stds[i]))


plt.figure(1)
plt.clf()
centro = (bins[:-1] + bins[1:]) / 2
plt.bar(centro, n_mean, align='center', width=(-bins[0]+bins[-1])/100)
plt.errorbar(bins[0:100] + 0.06, n_mean, yerr=n_std, fmt='.', color='g',
             label="Desviacion estandar")
plt.title('Distribucion W(x) con barras de error')
plt.xlabel('x')
plt.ylabel('W(x)')
plt.legend()
plt.savefig("Extra.jpg")
plt.show()

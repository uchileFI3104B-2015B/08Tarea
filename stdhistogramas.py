#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

DELTA = 4
N_puntos = 10000000
N_runs = 100

def W(x):
    exp1 = 3.5 * np.exp(-(np.power(x - 3, 2))/3)
    exp2 = 2 * np.exp(-(np.power(x + 1.5, 2))/0.5)
    return exp1 + exp2

def proposicion(xn):
    r = np.random.uniform(low=-1, high=1)
    return xn + r*DELTA

def calculo_hist(semilla):
    np.random.seed(semilla)
    X = np.zeros(N_puntos + 1)
    k = 0
    while k < N_puntos:
        s = np.random.uniform(low=0, high=1)
        xP = proposicion(X[k])
        if W(xP) / W(X[k]) > s:
            X[k+1] = xP
        else:
            X[k+1] = X[k]
        k += 1
    return np.histogram(X, bins=50, range=(-4, 8), normed=True)

x_w = np.linspace(-4, 8, 10000)
I = np.sqrt(np.pi) * (3.5*np.sqrt(3) + 2*np.sqrt(0.5))
h_result = np.zeros((50, N_runs))
for n in range(N_runs):
    hist_now = calculo_hist(n)
    print "Run", n+1, "terminado"
    for i in range(50):
        h_result[i][n] = hist_now[0][i]
bins = hist_now[1]
hist_mean = np.zeros(50)
hist_std = np.zeros(50)
for i in range(50):
    hist_mean[i] = np.mean(h_result[i])
    hist_std[i] = np.std(h_result[i])

plt.clf()
plt.figure(1)
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist_mean, align='center', width=0.2, label="Histograma")
plt.errorbar(bins[0:50]+0.12, hist_mean, yerr=hist_std, fmt='.', color='g',
             label="Barras de error (desviacion estandar)")
plt.plot(x_w, W(x_w)/I, color='r', linewidth=2, label="Distribucion deseada")
plt.ylim([0, 0.37])
plt.title('Distribucion W(x) generada via Metropolis con error asociado')
plt.xlabel('x')
plt.legend()
plt.show()

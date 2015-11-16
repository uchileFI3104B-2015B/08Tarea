#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def W(x):
    '''
    Define la distribucion w(x)
    '''
    distribucion = (3.5 * np.exp(- (x - 3.)**2 / 3.) +
                    2 * np.exp(- (x + 1.5)**2 / 0.5))
    return distribucion


def normalizacion(inicio, fin):
    '''
    calcula la normalizacion de la funcion entro los puntos inicio y fin
    para 10000 puntos
    '''
    x = np.linspace(inicio, fin, 10000)
    integral = integrate.trapz(W(x), x=x)
    return integral


def avanza_metropolis(xn, delta):
    xp = xn + delta * np.random.uniform(-1., 1.)
    if W(xp) / W(xn) > np.random.uniform(0., 1.):
        return xp
    else:
        return xn


def encuentra_delta_optimo(N_pruebas, d_minimo, d_maximo):
    '''
    Calcula el factor d para el cual se rechazan o aceptan
    la mitad de las pruebas
    '''

    Deltas = np.linspace(d_minimo, d_maximo, N_pruebas)
    Porcentaje = 0
    datos = np.zeros(N_pruebas)
    j = 0
    while np.fabs(Porcentaje - 50.) >= 0.001:
        aceptados = 0
        rechazados = 0
        datos[0] = np.random.uniform(-10., 10.)
        for i in range(1, N_pruebas):
            datos[i] = avanza_metropolis(datos[i-1], Deltas[j])
            if datos[i] == datos[i-1]:
                aceptados += 1
            else:
                rechazados += 1

        Porcentaje = 100 * aceptados / N_pruebas
        j += 1
        print j

    return Deltas[j]


# Se calcula la distribucion
Pasos = 1000000
delta = encuentra_delta_optimo(1000, -10, 10)
norm = normalizacion(-500, 500)
X = np.linspace(-7., 10., Pasos)
Datos = np.zeros(Pasos)
Datos[0] = np.random.uniform(-10., 10.)
distribucion = np.zeros(Pasos)
for i in range(1, Pasos):
    Datos[i] = avanza_metropolis(Datos[i-1], delta)
    distribucion[i] = W(X[i]) / norm


plt.figure(1)
n, bins, patches = plt.hist(Datos, 100, normed=1, facecolor='green', alpha=0.5)
plt.plot(X, distribucion, 'r')
plt.xlabel("$x$")
plt.ylabel("$Probabilidad$")

plt.savefig("Histograma.eps")

plt.show()
plt.draw()

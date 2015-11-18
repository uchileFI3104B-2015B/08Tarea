
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def W_dist(x):
    '''
    Define la distribucion w(x)
    '''
    w = (3.5 * np.exp(- (x - 3.)**2 / 3.) + 2 * np.exp(- (x + 1.5)**2 / 0.5))
    return w


def normalizar(a, b):
    '''
    calcula la normalizacion de la funcion entro los puntos inicio y fin
    para 10000 puntos
    '''
    x = np.linspace(a, b, 10000)
    integral = integrate.trapz(W_dist(x), x=x)
    return integral


def avanza_metropolis(xn, delta):
    xp = xn + delta * np.random.uniform(-1., 1.)
    if W_dist(xp) / W_dist(xn) > np.random.uniform(0., 1.):
        return xp
    else:
        return xn

def find_delta_opt(N_pruebas, d_minimo, d_maximo):
    '''
    Calcula el factor d rara para el cual se aceptan
    la mitad de las pruebas
    '''

    Deltas = np.linspace(d_minimo, d_maximo, N_pruebas)
    Porcentaje = 0
    datos = np.zeros(N_pruebas)
    j = 0
    while np.fabs(Porcentaje - 50.) >= 0.001:
        aceptados = 0
        datos[0] = np.random.uniform(-10., 10.)
        for i in range(1, N_pruebas):
            datos[i] = avanza_metropolis(datos[i-1], Deltas[j])
            if datos[i] == datos[i-1]:
                aceptados += 1
        Porcentaje = 100 * aceptados / N_pruebas
        j += 1

    return Deltas[j]

semilla=16450
np.random.seed(semilla)
Pasos = 10000000
delta = find_delta_opt(1000, -10, 10)
norm = normalizar(-500, 500)
X = np.linspace(-7., 10., Pasos)
Datos = np.zeros(Pasos)
Datos[0] = np.random.uniform(-10., 10.)
distribucion = np.zeros(Pasos)
for i in range(1, Pasos):
    Datos[i] = avanza_metropolis(Datos[i-1], delta)
    distribucion[i] = W_dist(X[i]) / norm


a = plt.figure(1)
a.clf()
b = a.add_subplot(111)
n, bins, patches = b.hist(Datos, 81, normed=True,
                            color='cyan', label="Histograma")
b.plot(X, distribucion, color='magenta', linewidth=2, label="Distribucion w(x)")
plt.xlabel("$x$")
plt.ylabel("$Probabilidad$")
plt.title('Distribucion W(x) y generada por Metropolis')
plt.legend()
plt.savefig("Histograma.eps")

plt.show()
plt.draw()

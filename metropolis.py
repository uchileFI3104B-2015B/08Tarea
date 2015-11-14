#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################################################################
#                                TAREA 8                                    #
#############################################################################

'''
Universidad de Chile
Facultad de Ciencias Fisicas y Matematicas
Departamento de Fisica
FI3104 Metodos Numericos para la Ciencia y la Ingenieria
Semestre Primavera 2015

Nicolas Troncoso Kurtovic
'''

import matplotlib.pyplot as p
import numpy as np
from scipy import integrate as sci

#############################################################################
#                                                                           #
#############################################################################

np.random.seed(251093)


def w(x):
    '''
    Funcion distribucion. La normalizacion fue calculada entre -100 y 100.
    '''
    a = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-(x + 1.5)**2 / 0.5)
    norm = 13.2515587081
    return a / norm


def un_paso_metropolis(w, xn, d):
    '''
    Un paso segun algoritmo de Metropolis.
    - Input: (funcion, semilla, distancia)
    - Output: xn o xp, segun criterio metropolis
    En base a un 'xn' dado evalua un 'xp' nuevo generado de manera random
    ubicado en un conjunto [xn - d, xn + d]. Si el xp cumple el criterio de
    Metropolis, retorna xp, en caso contrario retorna xn.
    '''
    r = np.random.uniform(-1., 1.)
    xp = xn + d * r
    filtro = np.random.uniform(0., 1.)
    if w(xp) / w(xn) > filtro:
        return xp
    else:
        return xn


def generador(w, xn, N, d):
    '''
    Generador de funcion distribucion.
    - Input: (funcion, xn semilla, Numero de bins, distancia pasos)
    - Output: Arreglo 'y' distribuido segun w, porcentaje de pasos aceptados
    '''
    y = np.zeros(N)
    # Guardar la primera semilla
    y[0] = np.copy(xn)
    # Contador de aceptados y rechazados respectivamente
    j = 0.
    k = 0.
    for i in range(len(y)-1):
        y[i+1] = un_paso_metropolis(w, y[i], d)
        if y[i+1] == y[i]:
            k += 1.
        else:
            j += 1.
    porcentaje = 100. * j / (j + k)
    return y, porcentaje


def calculador_d(dmin, dmax, N):
    '''
    Porcentaje de aceptados en funcion de la distancia de los pasos.
    - Input: (dmin, dmax, Numero pasos)
    - Output: Arreglo de distancias 'D', Arreglo de porcentajes 'P'
    '''
    D = np.linspace(dmin, dmax, N)
    P = np.zeros(len(D))
    for i in range(len(D)):
        y2, porcentaje = generador(w, 0., 10**5, D[i])
        P[i] = np.copy(porcentaje)
    return D, P


#############################################################################
#                                                                           #
#############################################################################


# Encontrar d optimo. Se encuentra d = 3.96
D, P = calculador_d(3., 5., 50)
p.plot(D, P, '.')
p.xlabel("Distancia pasos $d$")
p.ylabel("Porcentaje aceptados")
p.show()


# Vectores a utilizar
x = np.linspace(-10., 10., 10**6)
y1 = w(x)
y2, porcentaje = generador(w, 0., 10**7, 3.96)


# Integral para calcular normalizacion
integral = sci.trapz(y1, x=x)
print integral


# Ploteo
fig1 = p.figure()
fig1.clf()
n, bins, patches = p.hist(y2, normed=1, bins=10**2)
p.plot(x, y1, 'r')
p.xlabel("$x$")
p.ylabel("$W(x)$")
p.show()

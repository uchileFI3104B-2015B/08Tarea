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
    Funcion distribucion
    '''
    a = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-(x + 1.5)**2 / 0.5)
    norm = 13.2515587081
    return a / norm


def un_paso_metropolis(w, xn, d):
    '''
    Algoritmo de Metropolis. En base a un 'xn' dado evalua un 'xp' nuevo
    generado de manera random ubicado en un conjunto [xn - d, xn + d].
    Si el xp cumple el criterio de Metropolis, retorna xp, en caso contrario
    retorna xn.
    '''
    r = np.random.uniform(-1., 1.)
    xp = xn + d * r
    filtro = np.random.uniform(0., 1.)
    if w(xp) / w(xn) > filtro:
        return xp
    else:
        return xn


x = np.linspace(-10., 10., 10**6)
y = w(x)

integral = sci.trapz(y, x=x)
print integral

p.plot(x, y)
p.show()




























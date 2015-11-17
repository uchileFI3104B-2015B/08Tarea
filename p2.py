#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Aquí va el docstring de mi codigo explicando que cosas hace
'''
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def w_sin_normalizar(x):
    '''docstring'''
    return 3.5 * np.exp(-(x-3)**2 / 3) + 2 * np.exp(-(x-1.5)**2 / 0.5)


def normalizador(funcion, rango=[-100, 100]):
    '''Bla'''
    integral = scipy.integrate.quad(funcion, rango[0], rango[1])
    return integral


def w(x):
    '''bla'''
    return w_sin_normalizar(x) / normalizador(w_sin_normalizar)


def un_paso_metropolis(xn, delta, w):
    '''Docstring de esta funcion'''
    r = np.random.uniform(-1,1)
    xp = xn + delta * r

    # Criterio de Metrópolis:
    minimo_criterio = np.random.uniform(0,1)
    if (w(xp) / w(xn)) > minimo_criterio:
        return xp
    else:
        return xn

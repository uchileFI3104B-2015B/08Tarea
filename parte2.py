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
    w = 3.5 * np.exp(- (x - 3) ** 2 / 3) + 2 * np.exp(- (x + 1.5) ** 2 / 0.5)
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
    return w(x) / normalizar
    pass


def cond_metropolis(xn, d):
    '''
    aplica condicion de metropolis
    '''
    xp = xn + d * np.random.uniform(- 1, 1)
    if W(xp) / W(xn) > r:
        xn = xp
    return xn
    pass


def d_optimo():
    '''
    busca el paso optimo
    '''
    pass


# inicializacion


# iteracion

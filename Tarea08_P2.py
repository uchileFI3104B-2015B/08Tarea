#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def W(x, normalizacion):
    '''
    Define la distribucion w(x)
    '''
    distribuion = 3.5 * np.exp(- (x - 3.)**2 / 3.) + 2 * np.exp(- (x + 1.5)**2 / 0.5)
    return distribucion

def normalizacion(inicio,fin):
    '''
    calcula la normalizacion de la funcion entro los puntos inicio y fin
    para 10000 puntos
    '''
    x = np.linspace(inicio, fin, 10000)
    integral = integrate.trapz(W(x), x=x)

def avanza_metropolis(distribucion, xn, delta):
    xp = xn + r * np.random.uniform(-1., 1.)
    if W(xp)/W(xn) > np.random.uniform(0., 1.):
        return xp
    else :
        return xn

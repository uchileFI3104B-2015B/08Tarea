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
    distribucion = 3.5 * np.exp(- (x - 3.)**2 / 3.) + 2 * np.exp(- (x + 1.5)**2 / 0.5)
    return distribucion


def normalizacion(inicio, fin):
    '''
    calcula la normalizacion de la funcion entro los puntos inicio y fin
    para 10000 puntos
    '''
    x = np.linspace(inicio, fin, 10000)
    integral = integrate.trapz(W(x), x=x)


def avanza_metropolis(xn, delta):
    xp = xn + delta * np.random.uniform(-1., 1.)
    if W(xp) / W(xn) > np.random.uniform(0., 1.):
        return xp
    else :
        return xn



def encuentra_d_optimo(N_pruebas, d_minimo, d_maximo):
    '''
    Calcula el factor d para el cual se rechazan o aceptan
    la mitad de las pruebas
    '''
    norm = normalizacion(-500, 500)
    Deltas = np.linspace(d_minimo, d_maximo, N_pruebas)
    Porcentaje = 0
    datos = np.zeros(N_pruebas)
    j = 0
    while np.fabs(Porcentaje - 50.) >= 0.001:
        aceptados = 0
        rechazados = 0
        for i in range(1, N_pruebas):
            datos[i]=avanza_metropolis(datos[i-1], Deltas[j])
            if datos[i]==datos[i-1]:
                aceptados += 1
            else:
                rechazados += 1

        Porcentaje = 100 * aceptados / N_pruebas
        j += 1
        print j

    return Deltas[j]

d=encuentra_d_optimo(1000, -10,10)

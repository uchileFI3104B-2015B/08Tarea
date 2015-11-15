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

#############################################################################
#                                                                           #
#############################################################################


def in_toro(x, y, z):
    '''
    Retorna True si las coordenadas corresponden al interior del Toroide,
    retorna False si las coordenadas no estan al interior del Toroide.
    '''
    t = z**2 + (np.sqrt(x**2 + y**2) - 3.)**2
    if t <= 1:
        return True
    else:
        return False


def in_cilindro(x, y, z):
    '''
    Retorna True si las coordenadas corresponden al interior del Cilindro,
    retorna False si las coordenadas no estan al interior del Cilindro.
    '''
    c = (x - 2.)**2 + z**2
    if c <= 1:
        return True
    else:
        return False

def densidad(x, y, z):
    '''
    Densidad en el punto (x, y, z).
    '''
    return 0.5 * (x**2 + y**2 + z**2)


def montecarlo(densidad, N, xmin, xmax, ymin, ymax, zmin, zmax):
    '''
    Integra la funcion densidad dentro del cuerpo en una caja de volumen 2*10*2=V
    usando el metodo de montecarlo con N muestras.
    Entrega la masa total dentro del cuerpo formado por el toro y el cilindro
    y la posicion del centro de masa en (x, y, z)
    '''
    V = np.fabs(xmax - xmin) * np.fabs(ymax - ymin) * np.fabs(zmax - zmin)
    m = 0.
    xm = 0.
    ym = 0.
    zm = 0.
    for i in range(N): # para las N muestras
        x = np.random.uniform(xmin, xmax)
        y = np.random.uniform(ymin, ymax)
        z = np.random.uniform(zmin, zmax)
        if in_toro(x, y, z) and in_cilindro(x, y, z):
            dm = densidad(x, y, z)
            m += dm
            xm += x * dm
            ym += y * dm
            zm += z * dm
    CMx = (xm / m) * (V / N**3)
    CMy = (ym / m) * (V / N**3)
    CMz = (zm / m) * (V / N**3)
    return m, CMx, CMy, CMz


#############################################################################
#                                                                           #
#############################################################################
# Calculo de posicion
N = 10**6


# montecarlo(densidad, N, xmin, xmax, ymin, ymax, zmin, zmax)
m, CMx, CMy, CMz = montecarlo(densidad, N, 1., 3., -4., 4., -1., 1.)

print m, CMx, CMy, CMz

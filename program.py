#!/usr/bin/env python
# -*- coding: utf-8 -*-

# se importan librerias a usar

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def torito(x, y, z, R=3, r=1, dentro=1):
    '''
    El toro se asemeja a una dona, su ecuacion en coordenadas cartesianas es
    (R - ( x^2 + y^2)^(0.5) = r^2), donde R es la distancia desde el centro
    del toro hasta el centro del conducto. Y r es el radio del conducto.
    Esta función ve si un punto dado (x, y, z) está dentro o fuera del toro.
    '''
    ec = (R**2 - np.sqrt(x**2 + y**2))**2 + z**2
    A = 4 * np.pi**2 * r * R  # Corresponde al area del toro
    V = 2 * np.pi**2 * R * r**2  # Corresponde al volumen del toro
    if dentro == 1:
        if ec <= r**2:
            return 1
        else:
            return -1
    else:
        return A, V


def cilindrito(x, y, z, R=1):
    '''
    Similar a la funcion torito, pero con un cilindrito..
    R es el radio del cilindro y no hay h porque es infinito en el eje y.
    No tiene sentido hacer las funciones area y volumen, puesto que el
    cilindro es infinito en y
    '''
    ec = (x - 2)**2 + z**2
    if ec <= R:
        return 1
    else:
        return -1
#########################################################################
#  Ahora usando el método de montecarlo se integrara para encontrar     #
#  el centro de masa del volumen con densidad no lineal de              #
#  p = 0.5 * (x**2 + y**2 + z**2)                                       #
#########################################################################

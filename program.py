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
    A = 4 * np.pi**2 * r * R  # Corresponde al area del toro
    V = 2 * np.pi**2 * R * r**2  # Corresponde al volumen del toro
    if dentro == 1:
         return (R - np.sqrt(x**2 + y**2))**2 + z**2 <= 1
    else:
        return A, V


def cilindrito(x, y, z, R=1):
    '''
    Similar a la funcion torito, pero con un cilindrito..
    R es el radio del cilindro y no hay h porque es infinito en el eje y.
    No tiene sentido hacer las funciones area y volumen, puesto que el
    cilindro es infinito en y
    '''
    return (x - 2)**2 + z**2 <= R**2


def solido(x, y, z):
    '''
    Nos dice si un punto x, y, z está dentro o fuera del solido formado por
    el toro y el cilindro.
    Devuelve 0 si esta afuera y 1 si esta dentro
    '''
    return cilindrito(x, y, z)*torito(x, y, z)


def densidad(x, y ,z):
    return 0.5 * (x**2 + y**2 + z**2)


#########################################################################
#  Ahora usando el método de montecarlo se integrara para encontrar     #
#  el centro de masa del volumen con densidad no lineal de              #
#  p = 0.5 * (x**2 + y**2 + z**2)                                       #
#########################################################################
def centro_de_masa(N=10000):
    # N grande
    volumen = 2 * 8 * 2  # se integrará sobre este volumen
    suma = np.array([0, 0, 0, 0])  # sumas en x, y, z y total
    varianza = np.array([0, 0, 0, 0])  # varianzas en x, y, z y total

    for i in range(0, N):
        x = np.random.uniform(0, 1) * 2 + 1  ####
        y = np.random.uniform(0, 1) * 8 - 4
        z = np.random.uniform(0, 1) * 2 - 1
        vector = np.array([x, y, z, 1])  # cumple una función auxiliar
        if solido(x, y, z) == 1:
            suma += vector * densidad(x, y, z)
            varianza += (vector * densidad(x, y, z))**2
    masa = volumen * suma / N
    centro = (masa / masa[3])[:3]
    VAR = volumen * np.sqrt((varianza / N**2) - (masa / N)**2 / N)
    print masa, centro, VAR
    error = masa / masa[3] * np.sqrt((VAR / masa)**2 +
                    (VAR[3] / masa[3])**2)
    return centro, error

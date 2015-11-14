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


def in_cilindro(x, y, z)
    '''
    Retorna True si las coordenadas corresponden al interior del Cilindro,
    retorna False si las coordenadas no estan al interior del Cilindro.
    '''
    c = (x - 2.)**2 + z**2
    if c <= 1:
        return True
    else:
        return False




















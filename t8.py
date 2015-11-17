#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''se debe describir el centro de masa de
la intersección de un toro y un cilindro'''

import numpy as np
import matplotlib.pyplot as plt
from __future__ import division


def densidad(x,y,z):
''' retorna el valor de la densidad'''
    return 0.5*(x**2 + y**2 + z**2)


def esta_en_toro(x,y,z):
    '''define si las coordenadas (x,y,z) estan en el toro, retorna verdadero o falso '''
    return z**2 + (np.sqrt(x**2 + y**2)-3) <= 1

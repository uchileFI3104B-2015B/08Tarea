# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 00:06:13 2015

@author: Administrador
"""

import numpy as np
import matplotlib.pyplot as plt

#def generar_punto placeholder

#def dentro_cuerpo placeholder

#Main

N = 10000 #Número de iteraciones
Vol = 8*np.pi
for i in range(N):
    x, y, z = generar_punto()
    den = 0.5 * (x**2+y**2+z**2)
    if dentro_cuerpo:
        
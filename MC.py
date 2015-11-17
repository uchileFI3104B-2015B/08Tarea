# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 00:06:13 2015

@author: Administrador
"""

import numpy as np
import matplotlib.pyplot as plt

def generar_puntos(semilla, N):
    np.random.seed(semilla)
    x = np.random.uniform(low=1.0, high=3.1, size=N)
    y = np.random.uniform(low=-4, high=4.1, size=N)
    z = np.random.uniform(low=-1.0, high=1.1, size=N)
    return (x, y, z)

def dentro_toro(x, y, z):
    return (z**2 + (np.sqrt(x**2 + y**2) - 3)**2) <= 1

def dentro_cilindro(x, y, z):
    return ((x - 2)**2 + z**2) <= 1
    
#Main

N_p = 100000 #Número de puntos

def calculo_centro_masa(semilla, N):
    '''
    Esta función calucla el centro de masa usando Monte Carlo 1
    '''
    x, y, z = generar_puntos(semilla, N)
    P_adentro = {}
    for i in range(N_p):
        if dentro_toro(x[i], y[i], z[i]) and dentro_cilindro(x[i], y[i], z[i]):
            densidad = 0.5 * (x[i]**2 + y[i]**2 + z[i]**2)
            P_adentro[(x[i], y[i], z[i])] = densidad
    suma_x = 0
    suma_y = 0
    suma_z = 0
    M = 0 # Masa
    for p in P_adentro:
        suma_x += p[0]*P_adentro[p]
        suma_y += p[1]*P_adentro[p]
        suma_z += p[2]*P_adentro[p]
        M += P_adentro[p]
    x_CM = suma_x/M
    y_CM = suma_y/M
    z_CM = suma_z/M
    return (x_CM, y_CM, z_CM)
        
        
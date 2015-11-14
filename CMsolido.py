#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

np.random.seed(347)
N_puntos = 1000000

def in_toro(x, y, z):
    return z**2 + (np.sqrt(x**2 + y**2) - 3)**2 <= 1

def in_cilindro(x, z):
    return (x - 2)**2 + z**2 <= 1

def densidad(x, y, z):
    return 0.5 * (x**2 + y**2 + z**2)

# Lanzar números al azar en volumen que encierre al toro

x = np.random.uniform(low=-4.1, high=4.1, size=N_puntos)
y = np.random.uniform(low=-4.1, high=4.1, size=N_puntos)
z = np.random.uniform(low=-1.1, high=1.1, size=N_puntos)
Puntos_adentro = {}
for i in range(N_puntos):
    if in_toro(x[i], y[i], z[i]) and in_cilindro(x[i], z[i]):
        Puntos_adentro[(x[i], y[i], z[i])] = densidad(x[i], y[i], z[i])

suma_x = 0
suma_y = 0
suma_z = 0
for punto in Puntos_adentro:
    suma_x += punto[0]*Puntos_adentro[punto]
    suma_y += punto[1]*Puntos_adentro[punto]
    suma_z += punto[2]*Puntos_adentro[punto]
x_CM = suma_x/(1.0*N_puntos)
y_CM = suma_y/(1.0*N_puntos)
z_CM = suma_z/(1.0*N_puntos)
print "x_CM =", x_CM
print "y_CM =", y_CM
print "z_CM =", z_CM

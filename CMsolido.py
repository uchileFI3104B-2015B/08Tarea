#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

N_puntos = 100000
N_calc = 100
N_start = 45

def in_toro(x, y, z):
    return z**2 + (np.sqrt(x**2 + y**2) - 3)**2 <= 1

def in_cilindro(x, z):
    return (x - 2)**2 + z**2 <= 1

def densidad(x, y, z):
    return 0.5 * (x**2 + y**2 + z**2)

# Lanzar números al azar en volumen que encierre al toro
def calcular_CM(semilla):
    np.random.seed(semilla)
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
    return (x_CM, y_CM, z_CM)

x = np.zeros(N_calc)
y = np.zeros(N_calc)
z = np.zeros(N_calc)
for n in range(N_calc):
    x[n], y[n], z[n] = calcular_CM(n + N_start)
print "x_CM =", np.mean(x), "+/-", np.std(x)
print "y_CM =", np.mean(y), "+/-", np.std(y)
print "z_CM =", np.mean(z), "+/-", np.std(z)

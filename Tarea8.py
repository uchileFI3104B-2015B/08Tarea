#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def densidad(x, y, z):
    rho = 0.5 * (x**2 + y**2 + z**2)
    return rho


def toro(x, y, z):
    '''
    Función que permite discenir si las coordenadas
    actuales se encuentran dentro del Toroide.
    Si están dentro del Toroide, estarán también
    dentro del cilindro.
    '''
    return z**2 + (np.sqrt(x**2 + y**2)-3) <= 1

# Setup

np.random.seed(123)

N = 100000
V = 2.0 * 8.0 * 2.0

sump = 0.
sumx = 0.
sumy = 0.
sumz = 0.

varp = 0.
varx = 0.
vary = 0.
varz = 0.

# Algoritmo de Monte Carlo tipo 1

for i in range(0, N):
    x = np.random.uniform(1, 3)
    y = np.random.uniform(-4, 4)
    z = np.random.uniform(-1, 1)
    if toro(x, y, z):
        sump += densidad(x, y, z)
        sumx += x * densidad(x, y, z)
        sumy += y * densidad(x, y, z)
        sumz += z * densidad(x, y, z)
        varp += (densidad(x, y, z))**2
        varx += (densidad(x, y, z) * x)**2
        vary += (densidad(x, y, z) * y)**2
        varz += (densidad(x, y, z) * z)**2

p = (V * sump) / N
x = (V * sumx) / N
y = (V * sumy) / N
z = (V * sumz) / N

erp = V * np.sqrt((varp / (N - sump)**2 / N) / N)
erx = V * np.sqrt((varx / (N - sumx)**2 / N) / N)
ery = V * np.sqrt((vary / (N - sumy)**2 / N) / N)
erz = V * np.sqrt((varz / (N - sumz)**2 / N) / N)

Err = [erp, erx, ery, erz]  # Errores

x_cm = x / p
y_cm = y / p
z_cm = z / p

print "Centro de masas ubicado en = (%s, %s, %s)" % (x_cm, y_cm, z_cm)
print "Con errores = (%s, %s, %s, %s)" % (erp, erx, ery, erz)
print "en peso, x, y, z respectivamente"

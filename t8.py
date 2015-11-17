#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''se debe describir el centro de masa de
la intersección de un toro y un cilindro'''

import numpy as np

np.random.seed(200)
def densidad(x, y, z):
    ''' retorna el valor de la densidad'''
    return 0.5*(x**2 + y**2 + z**2)


def esta_en_toro(x, y, z):
    '''define si las coordenadas (x,y,z)
    estan en el toro, retorna verdadero o falso '''
    return z**2 + (np.sqrt(x**2 + y**2)-3) <= 1


N = 1000
volumen = 2.0 * 8.0 * 2.0  # Largo de cada variables
# (x,y,z) dado los limites en donde se intersectan
sw = 0.
swx = 0.
swy = 0.
swz = 0.

vw = 0.
vwx = 0.
vwy = 0.
vwz = 0.
for i in range(0, N):
    x = np.random.uniform(1, 3)
    y = np.random.uniform(-4, 4)
    z = np.random.uniform(-1, 1)
    if esta_en_toro(x, y, z):
        sw += densidad(x, y, z)
        swx += x * densidad(x, y, z)
        swy += y * densidad(x, y, z)
        swz += z * densidad(x, y, z)

w = (volumen * sw) / N
x = (volumen * swx) / N
y = (volumen * swy) / N
z = (volumen * swz) / N

x_cm = x / w
y_cm = y / w
z_cm = z / w

print x_cm
print y_cm
print z_cm

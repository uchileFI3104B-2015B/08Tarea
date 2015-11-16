#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este codigo determina una estimacion del centro de masas de un toro intersectado
con un cilindro
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#funciones esenciales


def densidad(x, y, z):
    '''
    entrega la densidad del punto de coord (x, y, z)
    '''
    return 0.5 * (x ** 2 + y ** 2 + z ** 2)
    pass


def en_toro(x, y, z):
    return z ** 2 + (np.sqrt(x ** 2 + y ** 2) - 3) ** 2 <= 1


def en_cilindro(x, y, z):
    return (x - 2) ** 2 + z ** 2 <= 1


def en_cuerpo(x, y, z):
    '''
    verifica si el punto cumple la condicion de estar en el cuerpo
    '''
    return (en_toro(x, y, z) and en_cilindro(x, y, z))


# main
# inicializacion
n = 100
mx = 0
my = 0
mz = 0
m = 0
vmx = 0
vmy = 0
vmz = 0
vm = 0
dx = 1.; dy = 8.; dz = 2.
V = dx * dy * dz
# iteracion
for i in range(0, n):
    x = 2 + 1 * np.random.uniform(0., 1.)
    y = - 4 + 8 * np.random.uniform(0., 1.)
    z = - 1 + 2 * np.random.uniform(0., 1.)
    if en_cuerpo(x, y, z):
        m += densidad(x, y, z)
        mx += x * densidad(x, y, z)
        my += y * densidad(x, y, z)
        mz += z * densidad(x, y, z)
        vm += (densidad(x, y, z)) ** 2
        vmx += (x * densidad(x, y, z)) ** 2
        vmy += (y * densidad(x, y, z)) ** 2
        vmz += (z * densidad(x, y, z)) ** 2


M = V * m / n
Mx = V * mx / n
My = V * my / n
Mz = V * mz / n
VM = V * np.sqrt(np.fabs((vm / n - (m / n) ** 2) / n))
VMx = V * np.sqrt(np.fabs((vmx / n - (mx / n) ** 2) / n))
VMy = V * np.sqrt(np.fabs((vmy / n - (my / n) ** 2) / n))
VMz = V * np.sqrt(np.fabs((vmz / n - (mz / n) ** 2) / n))
Xcm = Mx / M
Ycm = My / M
Zcm = Mz / M
VXcm = (Mx / M) * np.sqrt((VMx / Mx) ** 2 + (VM / M) ** 2)
VYcm = (My / M) * np.sqrt((VMy / My) ** 2 + (VM / M) ** 2)
VZcm = (Mz / M) * np.sqrt((VMz / Mz) ** 2 + (VM / M) ** 2)
print VXcm
print VYcm
print VZcm

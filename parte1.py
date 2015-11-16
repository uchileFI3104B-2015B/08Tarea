#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este codigo determina una estimacion del centro de masas de un toro intersectado
con un cilindro
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
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


def varianza(V, n, m, vm):
    return V * np.sqrt(np.fabs((vm / n - (m / n) ** 2) / n))


def error(M, VM, Mi, VMi):
    '''
    calcula el error con el tratamiento adecuado
    '''
    return (Mi / M) * np.sqrt((VMi / Mi) ** 2 + (VM / M) ** 2)


def centro_masa(V, n):
    mx = 0; my = 0; mz = 0; m = 0
    vmx = 0; vmy = 0; vmz = 0; vm = 0
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
    VM = varianza(V, n, m, vm)
    VMx = varianza(V, n, mx, vmx)
    VMy = varianza(V, n, my, vmy)
    VMz = varianza(V, n, mz, vmz)
    Xcm = Mx / M
    Ycm = My / M
    Zcm = Mz / M
    VXcm = error(M, VM, Mx, VMx)
    VYcm = error(M, VM, My, VMy)
    VZcm = error(M, VM, Mz, VMz)
    CM = Xcm, Ycm, Zcm
    VCM = VXcm, VYcm, VZcm
    return CM, VCM

# main
# inicializacion
n = 100
dx = 1.; dy = 8.; dz = 2.
V = dx * dy * dz
r, vr = centro_masa(V, n)


print r
print vr

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
    Retorna True si las coordenadas ingresadas corresponden al interior del
    Toroide, retorna False en caso contrario.
    '''
    t = z**2 + (np.sqrt(x**2 + y**2) - 3.)**2
    if t <= 1:
        return True
    else:
        return False


def in_cilindro(x, y, z):
    '''
    Retorna True si las coordenadas ingresadas corresponden al interior del
    Cilindro, retorna False en caso contrario.
    '''
    c = (x - 2.)**2 + z**2
    if c <= 1:
        return True
    else:
        return False


def densidad(x, y, z):
    '''
    Densidad en el punto (x, y, z).
    '''
    return 0.5 * (x**2 + y**2 + z**2)


def un_montecarlo(N):
    '''
    Integra la funcion densidad dentro del cuerpo en una caja de volumen V
    que contiene la interseccion del toroide y el cilindro. El metodo
    utilizado corresponde al metodo de montecarlo simple con N muestras.
    Entrega la masa total dentro del cuerpo formado por el toro y el cilindro
    y la posicion del centro de masa en (x, y, z)
    '''
    V = 2. * 8. * 2.
    m = 0.
    xm = 0.
    ym = 0.
    zm = 0.
    for i in range(int(N)):
        x = np.random.uniform(1., 3.)
        y = np.random.uniform(-4., 4.)
        z = np.random.uniform(-1., 1.)
        if in_toro(x, y, z) and in_cilindro(x, y, z):
            dm = densidad(x, y, z)
            m += dm
            xm += x * dm
            ym += y * dm
            zm += z * dm
    cmx = (xm / m)
    cmy = (ym / m)
    cmz = (zm / m)
    return (m * V / float(N)), cmx, cmy, cmz


def montecarlo(n, N):
    '''
    Repite la integracion de montecarlo con 'N' muestras un total de 'n'
    veces para poder calcular error std.
    '''
    masa = np.zeros(n)
    cmx = np.zeros(n)
    cmy = np.zeros(n)
    cmz = np.zeros(n)
    for i in range(n):
        masa[i], cmx[i], cmy[i], cmz[i] = un_montecarlo(N)
    std_masa = np.std(masa)
    M = np.mean(masa)
    std_x = np.std(cmx)
    std_y = np.std(cmy)
    std_z = np.std(cmz)
    rx = np.mean(cmx)
    ry = np.mean(cmy)
    rz = np.mean(cmz)
    return std_masa, M, rx, ry, rz, std_x, std_y, std_z


#############################################################################
#                                                                           #
#############################################################################

# Calculo de posicion
np.random.seed(251093)
# N = 10.**8
# 70.9711328071 2.08024710617 0.000735059915371 2.04809129067e-05
# N = 10.**7
# 70.9490120334 2.08027360481 -0.000125896812728 -0.000293288309803
#N = 10.**6
# 70.9855611903 2.0806898348 -0.00129049358625 -0.000699745899886

N = 10.**5
n = 1000

std_masa, M, rx, ry, rz, std_x, std_y, std_z = montecarlo(n, N)
print 'n = ', n
print 'N = ', N
print 'masa = ', M
print 'std_masa = ', std_masa
print 'rx = ', rx
print 'ry = ', ry
print 'rz = ', rz
print 'std_x = ', std_x
print 'std_y = ', std_y
print 'std_z = ', std_z

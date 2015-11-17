#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este codigo determina una estimacion del centro de masas de un toro
intersectado con un cilindro
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def en_toro(x, y, z):
    '''
    Recibe coordenadas x, y, z y retorna True si se encuentra en el toro
    de lo contrario retorna False
    '''
    return z ** 2 + (np.sqrt(x ** 2 + y ** 2) - 3) ** 2 <= 1


def en_cilindro(x, y, z):
    '''
    Recibe coordenadas x, y, z y retorna True si se encuentra en el cilindro
    de lo contrario retorna False
    '''
    return (x - 2) ** 2 + z ** 2 <= 1

def en_interseccion(x, y, z):
    '''
    Recibe coordenadas x, y, z y retorna True si se encuentra en la
    interseccion del toro y el cilindro, de lo contrario retorna False
    '''
    return (en_toro(x, y, z) and en_cilindro(x, y ,z))

def densidad(x, y, z):
    '''
    Recibe un punto (x, y, z) y entrega la densidad asociada a aquel
    '''
    return 0.5 * (x ** 2 + y ** 2 + z ** 2)

def varianza(V, n, m, vm):
    '''
    Calcula varianza
    '''
    return V * np.sqrt(np.fabs((vm / n - (m / n) ** 2) / n))


def error(M, VM, M_i, VM_i):
    '''
    calcula el error con el tratamiento adecuado
    '''
    return (M_i / M) * np.sqrt((VM_i / M_i) ** 2 + (VM / M) ** 2)

def centro_masa(V, n_steps):
    '''
    Recibe un volumen inicial minimo y una cantidad de pasos n
    con esto calcula el centro de masa de la caja en la que
    se encuentra la interseccion
    '''
    # inicializa sumas de densidad y varianza de esta por coordenada
    sum_x = 0
    sum_y = 0
    sum_z = 0
    sum_total = 0
    var_x = 0
    var_y = 0
    var_z = 0
    var_total = 0

    for i in range(0, n_steps):
        x = 1 + 2 * np.random.uniform(0., 1.)
        y = - 4 + 8 * np.random.uniform(0., 1.)
        z = - 1 + 2 * np.random.uniform(0., 1.)
        if en_interseccion(x, y, z):
            sum_total += densidad(x, y, z)
            sum_x += x * densidad(x, y, z)
            sum_y += y * densidad(x, y, z)
            sum_z += z * densidad(x, y, z)
            var_total += (densidad(x, y, z)) ** 2
            var_x += (x * densidad(x, y, z)) ** 2
            var_y += (y * densidad(x, y, z)) ** 2
            var_z += (z * densidad(x, y, z)) ** 2
    # Define variables para calcular facilmente coordenadas de centro de masa
    #
    M = V * sum_total / n_steps
    Mx = V * sum_x / n_steps
    My = V * sum_y / n_steps
    Mz = V * sum_z / n_steps
    V_M = varianza(V, n_steps, sum_total, var_total)
    V_Mx = varianza(V, n_steps, sum_x, var_x)
    V_My = varianza(V, n_steps, sum_y , var_y)
    V_Mz = varianza(V, n_steps, sum_z, var_z)
    X = Mx / M
    Y = My / M
    Z = Mz / M
    VX = error(M, V_M, Mx, V_Mx)
    VY = error(M, V_M, My, V_My)
    VZ = error(M, V_M, Mz, V_Mz)
    CM = X, Y, Z
    VCM = VX, VY, VZ
    return CM, VCM


# main

# inicializacion de pasos y volumen minimo
N_steps = 1000000
dx = 2.
dy = 8.
dz = 2.
V = dx * dy * dz
posicion, vr = centro_masa(V, N_steps)
print "Coordenadas centro de masa: " posicion
print "Error estimado para cada coordenada: " vr

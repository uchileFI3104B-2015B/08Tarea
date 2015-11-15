#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Estimacion del dentro de masa de un solido descrito por la interseccion de un
toro y un cilindro usando el metodo de monte-carlo
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def Dentro_del_toro(x,y,z,R,r):
    '''
    verifica si el punto (x,y,z) se encuentr dentro del toro de ecuacion
    (sqrt{ x^2 + y^2 } - R)^2 + z^2 = r^2
    returno TRUE si esta dentro y FALSE si no lo esta
    '''
    return (np.sqrt(x**2 + y**2) - R)**2 + z**2 <= r**2


def Densidad(x,y,z):
    '''
    retorna el valor de la densidad en el punto (x,y,z)
    '''
    return 0.5*(x**2 + y**2 + z**2)


# se define el volumen minimo que encierra la interseccion

N_steps=10000
volumen=3. * 8. * 2.

suma_peso = 0.
suma_x = 0.
suma_y = 0.
suma_z = 0.
varianza_peso = 0.
varianza_x = 0.
varianza_y = 0.
varianza_z = 0.

for i in range(0,N_steps):
    x = 1. + 3. * np.random.uniform(low=0, high=1, size=1)
    y = 8. * np.random.uniform(low=0, high=1, size=1) - 4.
    z = 2. * np.random.uniform(low=0, high=1, size=1) - 1.
    if Dentro_del_toro(x,y,z,3,1):
        suma_peso += Densidad(x,y,z)
        suma_x += x * Densidad(x,y,z)
        suma_y += y * Densidad(x,y,z)
        suma_z += z * Densidad(x,y,z)
        varianza_peso += np.sqrt(Densidad(x,y,z))
        varianza_x += np.sqrt(x * Densidad(x,y,z))
        varianza_y += np.sqrt(y * Densidad(x,y,z))
        varianza_z += np.sqrt(z * Densidad(x,y,z))

peso = volumen * suma_peso / N_steps
x = volumen * suma_x / N_steps
y = volumen * suma_y / N_steps
z = volumen * suma_z / N_steps
error_peso = volumen * np.sqrt((varianza_peso / N_steps -
                                np.sqrt(suma_peso / N_steps))/N_steps)
error_x = volumen * np.sqrt((varianza_x / N_steps -
                                np.sqrt(suma_x / N_steps))/N_steps)
error_y = volumen * np.sqrt((varianza_y / N_steps -
                                np.sqrt(suma_y / N_steps))/N_steps)
error_z = volumen * np.sqrt((varianza_z / N_steps -
                                np.sqrt(suma_z / N_steps))/N_steps)

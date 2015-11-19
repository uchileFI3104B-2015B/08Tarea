
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

''' Script que resuelve la parte 1 del centro de masa de un cuerpo solido
ocupando monte carlo '''


def in__toro(x, y, z, R, r):
    '''True si esta dentro de toro ,false si no'''

    return (np.sqrt(x**2 + y**2) - R)**2 + z**2 <= r**2


def in__cilindro(x, z, rho):
    ''' True si esta dentro del cilindro, o False en caso contrario'''

    return (x-2)**2 + z**2 <= rho**2


def Densidad(x, y, z):
    ''' Retorna el valor de la densidad en el punto (x,y,z)'''

    return 0.5*(x**2 + y**2 + z**2)


''' Funcion que calcula el centro de masa dependiendo de la semilla elegida'''


def calculo_cmasa(semilla):
    N_steps = 100000
    np.random.seed(semilla)
    x = 1 + 3 * np.random.uniform(0, 1, N_steps)
    y = 8 * np.random.uniform(0, 1, N_steps) - 4
    z = 2 * np.random.uniform(0, 1, N_steps) - 1
    vector_in = {}
    for i in range(N_steps):
        if in__toro(x[i], y[i], z[i], 3, 1) and in__cilindro(x[i], z[i], 1):
            vector_in[(x[i], y[i], z[i])] = Densidad(x[i], y[i], z[i])

    suma_dens = 0
    suma_x = 0
    suma_y = 0
    suma_z = 0
    for vector in vector_in:
        suma_dens += vector_in[vector]
        suma_x += vector[0]*vector_in[vector]
        suma_y += vector[1]*vector_in[vector]
        suma_z += vector[2]*vector_in[vector]

    X_cm = suma_x / suma_dens
    Y_cm = suma_y / suma_dens
    Z_cm = suma_z / suma_dens
    return (X_cm, Y_cm, Z_cm)

''' calcula N veces los centro de masa
y aplica estadistica para los errores asociados a Rcm '''
N = 120
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)

for n in range(N):
    x[n], y[n], z[n] = calculo_cmasa(n)

print "R_centro_masa = ", (np.mean(x), np.mean(y), np.mean(z))
print "con un error de ", (np.std(x), np.std(y), np.std(z))
print " en sus coordenadas respectivas"

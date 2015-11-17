'''
Estimacion del centro de masa de la interseccion de cilindro y un toro en donde las
integrales son calculadas con el metodo de Montecarlo
'''

from __future__ import division
import numpy as np

np.random.seed(100)


def densidad(x, y, z):
    '''
    Entrega la densidad del punto (x, y, z)
    '''
    return 0.5 * (x**2 + y**2 + z**2)


def toro(x, y, z):
    '''
    Retorna True si el punto (x, y, z) esta en el toro
    '''
    return (z**2) + ((np.sqrt(x**2 + y**2) - 3)**2) <= 1


def cilindro(x, y, z):
    '''
    Retorna True si el punto (x, y, z) esta en el cilindro
    '''
    return (x - 2)**2 + z**2 <= 1


def inter(x, y, z):
    '''
    La union de los dos casos anteriores
    '''
    return toro(x, y, z) and cilindro(x, y, z)


def err(V, n, m, f):
    '''
    El error asociado al Metodo de Montecarlo
    '''
    return V * np.sqrt(np.fabs(f - (m / n)) / n)


def error_div(a, delta_a, b, delta_b):
    '''
    Propagacion del error en una division
    '''
    return (a / b) * np.sqrt((delta_a / a) ** 2 + (delta_b / b) ** 2)


def centro_masa(V, n):

    '''
    Aca ocurre la magia, calculamos el centro de masa con las funciones auxiliares
    definidas anteriormente
    '''

    #valores iniciales
    mx = my = mz = m = 0
    f = fx = fy = fz = 0

    for i in range(0, n):

        x = 1 + 2 * np.random.uniform(0.0, 1.0)
        y = -4 + 8 * np.random.uniform(0.0, 1.0)
        z = -1 + 2 * np.random.uniform(0.0, 1.0)

        if inter (x, y, z) == True:

            d = densidad(x, y, z)

            m += d
            mx += x * d
            my += y * d
            mz += z * d

            f += d/n
            fx += (x*d)/n
            fy += (y*d)/n
            fz += (z*d)/n

    masa_t = (V*m)/n
    masa_x = (V*mx)/n
    masa_y = (V*my)/n
    masa_z = (V*mz)/n
    Xcm = masa_x/masa_t
    Ycm = masa_y/masa_t
    Zcm = masa_z/masa_t
    centro_de_masa = Xcm, Ycm, Zcm

    delta_m = err(V, n, m, f)
    delta_mx = err(V, n, mx, fx)
    delta_my = err(V, n, my, fy)
    delta_mz = err(V, n, mz, fz)

    error_x = error_div(masa_x, delta_mx, masa_t, delta_m)
    error_y = error_div(masa_y, delta_my, masa_t, delta_m)
    error_z = error_div(masa_z, delta_mz, masa_t, delta_m)
    error_asociado = error_x, error_y, error_z

    return centro_de_masa, error_asociado

n = 1000000
dx = 2.0
dy = 8.0
dz = 2.0
V = dx*dy*dz
P, E = centro_masa(V, n)
print 'La posicion del centro de masa:', P
print 'Y su error:', E

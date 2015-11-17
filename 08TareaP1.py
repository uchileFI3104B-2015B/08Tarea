	#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
'''
este script utiliza el algoritmo de monte carlo
para encontrar el centro de masa de un volumen
generado por la intersección de un toroide y un cilindro
'''


def montecarloP1(n):
    '''
    La funcion pide n : Cantidad de puntos a usar
    '''
    sw = swx = swy = swz = 0.0    # Variables
    varw = varx = vary = varz = 0.0  # Variables para calcular error
    vol = (np.pi*1.0)*(2*np.sqrt(15))   # Volumen de la region a usar
    for j in range(n):
        # puntos random
        x = 1.0+3.0*np.random.sample()
        y = (-np.sqrt(15))+2*np.sqrt(15)*np.random.sample()
        z = (-1.0)+2.0*np.random.sample()

        # condicion para ver si el punto x,y,z esta en el toroide
        if z**2+(np.sqrt(x**2+y**2)-3.0)**2 < 1.0:
            den = (1/2.)*(x**2)*(y**2)*(z**2)
            sw += den
            swx += x*den
            swy += y*den
            swz += z*den
            varw += (den)**2
            varx += (x*den)**2
            vary += (y*den)**2
            varz += (z*den)**2
    # valores de la integrales
    w = vol*sw/n
    x = vol*swx/n
    y = vol*swy/n
    z = vol*swz/n
    # valores de los errores
    dw = vol*np.sqrt((varw/n-(sw/n)**2)/n)
    dx = vol*np.sqrt((varx/n-(swx/n)**2)/n)
    dy = vol*np.sqrt((vary/n-(swy/n)**2)/n)
    dz = vol*np.sqrt((varz/n-(swz/n)**2)/n)
    print "El volumen es", w, "con un error de", dw
    print "La posicion del centro de masa es: (x,y,z)=",
    x/w, y/w, z/w,  "con un error de", dx, dy, dz


# main
# setup
n = 1000000       # Cantidad de puntos de la muestra
montecarloP1(n)

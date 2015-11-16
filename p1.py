#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Aquí va el docstring de mi codigo explicando que cosas hace
'''


def densidad(x, y, z):
    ''' Retorna la densidad del sólido en una coordenada dada '''
    rho = 0.5 + (x**2 + y**2 + z**2)
    return rho


def dentro_toro(x, y, z):
    '''Retorna True si las coordenadas están dentro del toro,
    y False si no lo está'''
    return z**2 + (sqrt(x**2 + y**2) - 3)**2 <= 1


def dentro_cilindro(x, y, z):
    '''Retorna True si las coordenadas están dentro del cilindro,
    y False si no lo está'''
    return (x-2)**2 + z**2 <= 1


def interseccion(x, y, z):
    '''Retorna True si las coordenadas estan en la interseccion del
    cilindro con el toro, y False si no'''
    return dentro_toro(x, y, z) and dentro_cilindro(x, y, z)


def MC1():
    ''' Utiliza el algoritmo de Montecarlo 1 para bla'''

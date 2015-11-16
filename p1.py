#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Aquí va el docstring de mi codigo explicando que cosas hace
'''

def densidad(x, y, z):
    ''' Retorna la densidad del sólido en una coordenada dada '''
    rho = 0.5 + (x**2 + y**2 + z**2)
    return rho

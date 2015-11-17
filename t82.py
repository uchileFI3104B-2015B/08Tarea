#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''utilizando el algoritmo de metropolis  Se desea obtener una muestra
aleatoria de números con la distribución
(no normalizada) w(x)'''

import numpy as np
import scipy.integrate as si


def fn_de_peso(x):
    return (3.5 * np.exp(-((x - 3)**2) / 3) + 2 * np.exp(-((x + 1.5)**2)/0.5))

a = -100
b = 100
integral=si.quad(fn_de_peso, a, b);
print integral

def fn_normalizada(x):
    return fn_de_peso(x) / 13.251558708069131

inte=si.quad(fn_normalizada,a,b)
print inte

def metropolis(delta,xn):
    xp = xn + delta *np.random.uniform(-1, 1)
    if fn_normalizada(xp) / fn_normalizada(xn) > np.random.uniform(0, 1):
        return xp
    else:
        return xn

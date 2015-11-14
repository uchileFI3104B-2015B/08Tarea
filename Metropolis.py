#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

np.random.seed(347)
DELTA = 2
N_puntos = 10000000

def W(x):
    return 3.5*np.exp(-((x - 3)**2)/3) + 2*np.exp(-((x + 1.5)**2)/0.5)

def proposicion(xn):
    r = np.random.uniform(low=-1, high=1)
    return xp = xn + r*DELTA

X = np.zeros(N_puntos)
n_aceptados = 0
n = 0
while n < N_puntos:
    s = np.random.uniform(low=0, high=1)
    xP = proposicion(X[n])
    if W(xP) / W(X[n]) > s:
        X[n+1] = xP
        n_aceptados += 1
    else:
        X[n+1] = X[n]
    n += 1

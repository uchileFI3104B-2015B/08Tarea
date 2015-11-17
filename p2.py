'''
Este script

'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

def W(x, norma):
    #Distribucion no normalizada
    W = 3.5 * np.exp(- (x - 3) ** 2 / 3.) + 2 * np.exp(- (x + 1.5) ** 2 / 0.5)
    W_norm = W / norma
    return W_norm


def metropolis(w, xn, delta):
    #Algoritmo del método Metrópolis
    r = np.random.uniform(-1, 1)
    xp = xn + delta * r
    criterio = np.random.uniform(0, 1)
    if w(xp) / w(xn) > criterio:
        return xp
    else:
        return xn


def calcula_delta():
    #Calcula el delta apropiado para aceptar 50 por ciento de las proposiciones


#Main

#Setup
n =
#Calcula la integral de W(x)
norma =

#Calcula Delta eficiente
delta = calcula_delta()

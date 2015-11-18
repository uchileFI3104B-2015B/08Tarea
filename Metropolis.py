# -*- coding: utf-8 -*-
"""
Este código recibe 
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(221)
N = 10000000 # Número de 
#delta = ??
 
def W(x):
    e1= 3.5 * np.exp(-(np.power(x - 3, 2))/3)
    e2= 2 * np.exp(-(np.power(x + 1.5, 2))/0.5)
    return e1 + e2

def proposicion(x_n): #Para Metropolis
    r = np.random.uniform(low=-1, high=1)
    return x_n + r*delta

#Main
 
x = np.zeros(N+1)
n_a = 0 #n aceptados
n = 0 # sirve como contador
while n < N:
    s = np.random.uniform(low=0, high=1)
    x_p = proposicion (x[n])
    if W(x_p) / W(x[n]) > s:
        x[n+1] = x_p
        n_a += 1
    else:
        x[n+1] = x[n]
    n += 1

W_p = np.sqrt(np.pi) * (3.5*np.sqrt(3) + 2*np.sqrt(0.5))
print "Numero de proposiciones aceptadas: ", n_a
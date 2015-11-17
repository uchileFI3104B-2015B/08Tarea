# -*- coding: utf-8 -*-
"""
Este código recibe 
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

np.random.seed(221)
N = 10000000
#delta = ??
 
def W(x):
    e1= 3.5 * np.exp(-(np.power(x - 3, 2))/3)
    e2= 2 * np.exp(-(np.power(x + 1.5, 2))/0.5)
    return e1 + e2

def proposicion(x_n): #Para Metropolis
    r = np.random.uniform(low=-1, high=1)
    return x_n + r*delta

#Main
 


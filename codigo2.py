'''
'''

from __future__ import division
import numpy as np


def w(x):
    return (3.5 * np.exp(( - (x - 3) ** 2) / 3) +
            2 * np.exp (- ((x + 1.5) ** 2) / 0.5))

def W(x):
    return w(x) / norma



n=1

x_int=np.linspace(-10, 10, 1000)
norma = np.trapz(w(x_int), x_int)

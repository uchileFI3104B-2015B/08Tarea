from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapz


def w(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion

x=np.linspace(-10,10,1e3)
integral = trapz(w(x), x=x)

def w_normalizado(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion / integral


fig = plt.figure(1)
fig.clf()
plt.plot(x,w_normalizado(x), '-o')
plt.show()
plt.draw()
plt.savefig('w(x)_normalizado.png')

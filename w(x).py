from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapz


def w(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion


def w_normalizado(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion / integral

def avanza_metropolis(w_normalizado, xn, delta):
    r = np.random.uniform(-1., 1.)
    xp = xn + delta * r
    gamma = np.random.uniform(0., 1.)
    if w(xp) / w(xn) > gamma:
        return xp
    else:
        return xn


# Se grafica W(x) normalizado
x=np.linspace(-10,10,1e3)
integral = trapz(w(x), x=x)
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111)
plt.plot(x,w_normalizado(x), '-o')
ax.set_xlabel("x")
ax.set_ylabel("W(x)")
plt.show()
plt.draw()
plt.savefig('w(x)_normalizado.png')

'''
Este script blablabla
'''
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(2308)


def en_cuerpo(x, y, z):
    #True si esta dentro del cuerpo (Toro and Cilindro), False si no
    return (z ** 2 + ((x **2 + y**2) ** 0.5 - 3)**2 <= 1 and
            (x - 2) ** 2 + z ** 2 <= 1)


def densidad(x, y, z):
    return 0.5 * (x ** 2 + y ** 2 + z **2)


def var(x, y, z):
    vw = densidad(x, y, z) ** 2
    vx = (densidad(x, y, z) * x) ** 2
    vy = (densidad(x, y, z) * y) ** 2
    vz = (densidad(x, y, z) * z) ** 2
    return (vw, vx, vy, vz)

sw=0
sx=0
sy=0
sz=0
varw=0
varx=0
vary=0
varz=0
V=2*8*2
n=1000000
for i in range(0, n):
    x = 1 + 3 * np.random.uniform(0., 1.)
    y = - 4 + 8 * np.random.uniform(0., 1.)
    z = - 1 + 2 * np.random.uniform(0., 1.)
    if en_cuerpo(x, y, z):
        sw += densidad(x, y, z)
        sx += x * densidad(x, y, z)
        sy += y * densidad(x, y, z)
        sz += z * densidad(x, y, z)
        varw += var(x, y, z)[0]
        varx += var(x, y, z)[1]
        vary += var(x, y, z)[2]
        varz += var(x, y, z)[3]

w = V * sw / n
x = V * sx / n
y = V * sy / n
z = V * sz / n

print x

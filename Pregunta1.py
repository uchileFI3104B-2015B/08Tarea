# -*- coding: utf-8 -*-
"""
Integración de un volumen generado por la intersección entre
un toro y un cilindro mediante el método de MonteCarlo.
"""

from __future__ import division
import numpy as np
import math

np.random.seed(7000)
N = 10000000
rand = np.random.uniform(low=0.0, high=1.0, size=N*3+3)
sw = swx = swy = swz = 0.0
varw = varx = vary = varz = 0.0
vol = math.pi * 8.
for j in range(1, N+1):
    x = 1. + 2.0 * rand[j * 3]
    y = (-4.0) + 8.0 * rand[j * 3 + 1]
    z = (-1.0) + 2.0 * rand[j * 3 + 2]
    if ((math.sqrt(x ** 2 + y ** 2) - 3.0) ** 2) - ((x - 2) ** 2) < 0.0:
        den = 0.5*((x**2)+(y**2)+(z**2))
        swx += x*den
        swy += y*den
        swz += z*den
        varx += (x*den)**2
        vary += (y*den)**2
        varz += (z*den)**2
x = vol * swx / N
y = vol * swy / N
z = vol * swz / N
dx = vol * math.sqrt((varx / N - (swx / N) ** 2) / N)
dy = vol * math.sqrt((vary / N - (swy / N) ** 2) / N)
dz = vol * math.sqrt((varz / N - (swz / N) ** 2) / N)
print x
print y
print z
print dx
print dy
print dz

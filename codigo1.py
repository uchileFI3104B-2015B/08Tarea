'''
Este script estima numericamente las coordenadas del centro de masa del cuerpo
producido por la interseccion de un
Toro: z ** 2 + ((x **2 + y**2) ** 0.5 - 3)**2 <= 1
y de un
Cilindro: (x - 2) ** 2 + z ** 2 <= 1
con una distribucion de densidad dada por 0.5 * (x ** 2 + y ** 2 + z **2)
'''
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# Designamos la semilla
np.random.seed(2308)


def en_cuerpo(x, y, z):
    # True si esta dentro del cuerpo (Toro and Cilindro), False si no
    return (z ** 2 + ((x ** 2 + y ** 2) ** 0.5 - 3) ** 2 <= 1 and
            (x - 2) ** 2 + z ** 2 <= 1)


def densidad(x, y, z):
    # Entrega el valor de la densidad para los distintos valores de x, y, z
    return 0.5 * (x ** 2 + y ** 2 + z ** 2)


def var(x, y, z):
    # Determina varianza de masa, x, y, z
    vw = densidad(x, y, z) ** 2
    vx = (densidad(x, y, z) * x) ** 2
    vy = (densidad(x, y, z) * y) ** 2
    vz = (densidad(x, y, z) * z) ** 2
    return (vw, vx, vy, vz)


# Main
# Setup

# Inicializo valores
sw = 0
swx = 0
swy = 0
swz = 0

varw = 0
varx = 0
vary = 0
varz = 0

# Volumen:
V = 2*8*2
n = 1e6

for i in range(0, int(n)):
    x = 1 + 3 * np.random.uniform(0., 1.)
    y = - 4 + 8 * np.random.uniform(0., 1.)
    z = - 1 + 2 * np.random.uniform(0., 1.)
    if en_cuerpo(x, y, z):
        var_i = var(x, y, z)
        den_i = densidad(x, y, z)
        sw += densidad(x, y, z)
        swx += x * den_i
        swy += y * den_i
        swz += z * den_i
        varw += var_i[0]
        varx += var_i[1]
        vary += var_i[2]
        varz += var_i[3]

w = V * sw / n          # Valor promedio de la masa
x = V * swx / n / w     # Valor promedio de coordenada x
y = V * swy / n / w     # Valor promedio de coordenada y
z = V * swz / n / w     # Valor promedio de coordenada z

# Errores asociados
dw = V * ((varw / n - (sw / n)) / n) ** 0.5
dx = V * ((varx / n - (swx / n)) / n) ** 0.5
dy = V * ((vary / n - (swy / n)) / n) ** 0.5
dz = V * ((varz / n - (swz / n)) / n) ** 0.5

# Errores asociados a los centro de masa
d_cm_x = (x / w) * (((dw / w) ** 2 + (dx / x) ** 2) ** 0.5)
d_cm_y = (y / w) * (((dw / w) ** 2 + (dy / y) ** 2) ** 0.5)
d_cm_z = (z / w) * (((dw / w) ** 2 + (dz / z) ** 2) ** 0.5)

# Muestra valores
print 'Centro de masa en x =', x, '+-', d_cm_x
print 'Centro de masa en y =', y, '+-', d_cm_y
print 'Centro de masa en z =', z, '+-', d_cm_z

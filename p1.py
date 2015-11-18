'''
Este script usa el método de Monte Carlo para estimar la posición del centro de
masa de un sólido descrito por la intersección de un toro y un cilindro,
cuya densidad varía según rho(x, y, z) = 0.5 * (x^2 + y^2 + z^2)
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)


def densidad(x, y, z):
    # Densidad en el punto (x,y,z)
    return 0.5 * (x ** 2 + y ** 2 + z ** 2)


def toro(x, y, z):
    # Region del toro
    return z ** 2 + (np.sqrt(x ** 2 + y ** 2) - 3) ** 2 <= 1


def cilindro(x, y, z):
    # Region del cilindro
    return (x - 2) ** 2 + z ** 2 <= 1


def solido(x, y, z):
    # Verifica que el punto (x,y,z) se encuentre en la region del solido
    # (interseccion del toro con el cilindro). Retorna True si está
    # y retorna False si es que no está.
    return (toro(x, y, z) and cilindro(x, y, z))


# Main

# Setup
# Valores de muestra deseados
n = 1000000
# Volumen del solido
dx = 2
dy = 8
dz = 2
V = dx * dy * dz
# Suma inicial para peso, x, y, z, y sus varianzas correspondientes
sum_masa = 0.
sum_x = 0.
sum_y = 0.
sum_z = 0.
var_masa = 0.
var_x = 0.
var_y = 0.
var_z = 0.

# Iteracion
for i in range(0, n):
    # Generar numeros al azar dentro del volumen que engloba al solido
    x = 1 + 2 * np.random.uniform(0., 1.)
    y = -4 + 8 * np.random.uniform(0., 1.)
    z = -1 + 2 * np.random.uniform(0., 1.)
    if solido(x, y, z):
        dens = densidad(x, y, z)
        sum_masa += dens
        sum_x += x * dens
        sum_y += y * dens
        sum_z += z * dens

        var_masa += (dens) ** 2
        var_x += (x * dens) ** 2
        var_y += (y * dens) ** 2
        var_z += (z * dens) ** 2

# Valores de las integrales
masa = V * sum_masa / n
x = V * sum_x / n
y = V * sum_y / n
z = V * sum_z / n

# Coordenadas del centro de masa
x_cm = x / masa
y_cm = y / masa
z_cm = z / masa

# Valores para el error asociado a los valores x, y, z y masa
d_masa = V * ((var_masa / n - ((sum_masa / n) ** 2)) / n) ** 0.5
d_x = V * ((var_x / n - ((sum_x / n) ** 2)) / n) ** 0.5
d_y = V * ((var_y / n - ((sum_y / n) ** 2)) / n) ** 0.5
d_z = V * ((var_z / n - ((sum_z / n) ** 2)) / n) ** 0.5

# Calculo del error para los valores del centro de masa con la formula
# de propagacion de errores en la division
error_x = (x / masa) * np.sqrt((d_x / x)**2 + (d_masa / masa)**2)
error_y = (y / masa) * np.sqrt((d_y / y)**2 + (d_masa / masa)**2)
error_z = (z / masa) * np.sqrt((d_z / z)**2 + (d_masa / masa)**2)

print 'Coordenadas x,y,z del centro de masa'
print x_cm, '= x_cm'
print y_cm, '= y_cm'
print z_cm, '= z_cm'
print 'Errores asociados a x,y,z'
print error_x, '= error x'
print error_y, '= error y'
print error_z, '= error z'

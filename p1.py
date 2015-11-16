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
    #Densidad en el punto (x,y,z)
    return 0.5 * (x ** 2 + y ** 2 + z ** 2)


def toro(x, y, z):
    #Region del toro
    return z ** 2 + (np.sqrt(x ** 2 + y ** 2) - 3) ** 2 <= 1


def cilindro(x, y, z):
    #Region del cilindro
    return (x - 2) ** 2 + z ** 2 <= 1


def solido(x, y, z):
    #Verifica que el punto (x,y,z) se encuentre en la region del solido
    #(interseccion del toro con el cilindro). Retorna True si está
    #y retorna False si es que no está.
    return (toro(x, y, z) and cilindro(x, y, z))




#Main

#Setup
#Valores de muestra deseados
n = 1000
#Volumen del solido
dx = 2
dy = 8
dz = 2
V = dx * dy * dz
#Suma inicial para peso, x, y, z, y sus varianzas correspondientes
sum_peso = 0.
sum_x = 0.
sum_y = 0.
sum_z = 0.
var_peso = 0.
var_x = 0.
var_y = 0.
var_z = 0.

#Iteracion
for i in range(0, n):
    x = 1 + 2 * np.random.uniform(0., 1.)
    y = -4 + 8 * np.random.uniform(0., 1.)
    z = -1 + 2 * np.random.uniform(0., 1.)
    if solido(x, y, z):
        sum_peso += densidad(x, y, z)
        sum_x += x * densidad(x, y, z)
        sum_y += y * densidad(x, y, z)
        sum_z += z * densidad(x, y, z)

        var_peso += (densidad(x, y, z)) ** 2
        var_x += (x * densidad(x, y, z)) ** 2
        var_y += (y * densidad(x, y, z)) ** 2
        var_z += (z * densidad(x, y, z)) ** 2

#Valores de las integrales
peso = V * sum_peso / n
x = V * sum_x / n
y = V * sum_y / n
z = V * sum_z / n

#Coordenadas del centro de masa
x_cm = x / peso
y_cm = y / peso
z_cm = z / peso

#Valores para el error asociado
dw = V * ((var_peso / n - ((sum_peso / n) ** 2)) / n) ** 0.5
dx = V * ((var_x / n - ((sum_x / n) ** 2)) / n) ** 0.5
dy = V * ((var_y / n - ((sum_y / n) ** 2)) / n) ** 0.5
dz = V * ((var_z / n - ((sum_z / n) ** 2)) / n) ** 0.5

print x_cm
print y_cm
print z_cm

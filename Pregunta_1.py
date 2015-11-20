"""
Script que estima el centro de masa de un solido generado por la interseccion
de un toro y un cilindro de ecuaciones:
toro: z^2+(sqrt(x^2+y^2)-3)^2
cilindro: (x-2)^2+z^2
La densidad del solido varia de la forma:
0.5*(x^2+y^2+z^2)
"""

from __future__ import division
import numpy as np


np.random.seed(7)


def densidad(x, y, z):
    """
    Retorna densidad en un punto dado de coordenadas (x,y,z)
    """
    return 0.5*(x**2+y**2+z**2)


def en_toro(x, y, z):
    """
    Retorna True si el punto (x,y,z) esta en el toro
    Retorna False si no esta en el toro.
    """
    toro = z**2+(np.sqrt(x**2+y**2)-3)**2
    if toro <= 1:
        return True
    else:
        return False


def en_cilindro(x, z):
    """
    Retorna True si el punto (x,y,z) esta en el cilindro.
    Retorna False si no esta en el cilindro
    """
    cilindro = (x-2)**2+z**2
    if cilindro <= 1:
        return True
    else:
        return False


# setup

n = 10000
suma_densidades = suma_x = suma_y = suma_z = 0
x_CM = np.zeros(100)
y_CM = np.zeros(100)
z_CM = np.zeros(100)

# limites del volumen sobre el que se integra
limite_x1 = 1
limite_x2 = 3
limite_y1 = -4
limite_y2 = 4
limite_z1 = -1
limite_z2 = 1

d_x = 2
d_y = 8
d_z = 2
volumen = d_x*d_y*d_z

# En cada iteracion se obtienen valores para las coordenadas del centro de masa

counter = 0
while counter < 100:
    for i in range(n):
        x = np.random.uniform(limite_x1, limite_x2)
        y = np.random.uniform(limite_y1, limite_y2)
        z = np.random.uniform(limite_z1, limite_z2)
        if en_toro(x, y, z) and en_cilindro(x, z):
            rho = densidad(x, y, z)
            suma_densidades += rho
            suma_x += x*rho
            suma_y += y*rho
            suma_z += z*rho
    masa = volumen*suma_densidades/n
    f_x = volumen*suma_x/n
    f_y = volumen*suma_y/n
    f_z = volumen*suma_z/n
    x_cm = f_x/masa
    y_cm = f_y/masa
    z_cm = f_z/masa
    x_CM[counter] = x_cm
    y_CM[counter] = y_cm
    z_CM[counter] = z_cm
    counter += 1
# Se promedian todos los valores obtenidos para  obteneer las coordenadas del
# centro de masa

promedio_x = np.mean(x_CM)
promedio_y = np.mean(y_CM)
promedio_z = np.mean(z_CM)

desviacion_estandar_x = np.std(x_CM)
desviacion_estandar_y = np.std(y_CM)
desviacion_estandar_z = np.std(z_CM)
# Muestra los valores obtenidos

print 'x_cm = ' + str(promedio_x) + '+-' + str(desviacion_estandar_x)
print 'y_cm = ' + str(promedio_y) + '+-' + str(desviacion_estandar_y)
print 'z_cm = ' + str(promedio_z) + '+-' + str(desviacion_estandar_z)

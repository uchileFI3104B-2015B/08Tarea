import numpy as n
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Arreglos numéricos para definir los puntos dentro del volumen
x = n.linspace(1, 3, 101)
y = n.linspace(-4, 4, 401)
z = n.linspace(-1, 1, 101)
# Variables para guardar datos
Puntos = []  # Guarda puntos que cumplen las condiciones
Densidades = []  # Guarda las densidades de cada uno de esos puntos
# Crea el "volumen" de puntosy evalua los que cumplan las condiciones
for a in x:
    for b in y:
        for c in z:
            if c**2 + ((a**2 + b**2)**(0.5) - 3)**2 <= 1:  # Toro
                if c**2 + (a - 2)**2 <= 1:  # Cilindro
                    Puntos.append([a, b, c])
# Calcula la densidad para cada punto
for a in Puntos:
    p = 0.5 * ((a[0])**2 + (a[1])**2 + (a[2])**2)
    Densidades.append(p)
# Variables para guardar las sumatorias
sumaX = 0
sumaY = 0
sumaZ = 0
sumaD = 0
# Obtiene las ponderaciones de distancia por densidad
for a in range(len(Puntos)):
    sumaX += Puntos[a][0]*Densidades[a]
    sumaY += Puntos[a][1]*Densidades[a]
    sumaZ += Puntos[a][2]*Densidades[a]
    sumaD += Densidades[a] # Suma todas las densidades
# Divide en cada eje por la densidad total
Xcm = sumaX / sumaD
Ycm = sumaY / sumaD
Zcm = sumaZ / sumaD
# Entrega el valor
print('El centro de masa esta en (' + str(round(Xcm, 3)) + ', ' +
      str(round(Ycm, 3)) + ', ' + str(round(Zcm, 3)) + ').')

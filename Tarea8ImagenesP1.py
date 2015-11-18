import numpy as n
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Arreglos para tomar todo el espacio en el que estan las figuras
x = n.linspace(-4, 4, 41)
y = n.linspace(-4, 4, 41)
z = n.linspace(-4, 4, 41)

Puntos = []
# Aca se modifica el codigo dependiendo de la figura
# Por defecto arma la intersección
for a in x:
    for b in y:
        for c in z:
            if c**2 + ((a**2 + b**2)**(0.5) - 3)**2 <= 1:
                if c**2 + (a - 2)**2 <= 1:
                    Puntos.append([a, b, c])

X = []
Y = []
Z = []
# Distribuye las coordenadas de cada punto
for a in range(len(Puntos)):
    X.append(Puntos[a][0])
    Y.append(Puntos[a][1])
    Z.append(Puntos[a][2])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)
plt.title('figura')
plt.show()

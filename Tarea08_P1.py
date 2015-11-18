#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Estimacion del dentro de masa de un solido descrito por la interseccion de un
toro y un cilindro usando el metodo de monte-carlo
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri


def Dentro_del_toro(x, y, z, R, r):
    '''
    verifica si el punto (x,y,z) se encuentr dentro del toro de ecuacion
    (sqrt{ x^2 + y^2 } - R)^2 + z^2 = r^2
    returno TRUE si esta dentro y FALSE si no lo esta
    '''
    return (np.sqrt(x**2 + y**2) - R)**2 + z**2 <= r**2


def Densidad(x, y, z):
    '''
    retorna el valor de la densidad en el punto (x,y,z)
    '''
    return 0.5*(x**2 + y**2 + z**2)


# se define el volumen minimo que encierra la interseccion

N_steps = 1000000
volumen = 2. * 8. * 2.

semilla = 16450
np.random.seed(semilla)

suma_peso = 0.
suma_x = 0.
suma_y = 0.
suma_z = 0.
varianza_peso = 0.
varianza_x = 0.
varianza_y = 0.
varianza_z = 0.

for i in range(0, N_steps):
    x = 1. + 2. * np.random.uniform(0., 1.)
    y = 8. * np.random.uniform(0., 1.) - 4.
    z = 2. * np.random.uniform(0., 1.) - 1.
    if Dentro_del_toro(x, y, z, 3, 1):
        suma_peso += Densidad(x, y, z)
        suma_x += x * Densidad(x, y, z)
        suma_y += y * Densidad(x, y, z)
        suma_z += z * Densidad(x, y, z)
        varianza_peso += Densidad(x, y, z)**2
        varianza_x += (x * Densidad(x, y, z))**2
        varianza_y += (y * Densidad(x, y, z))**2
        varianza_z += (x * Densidad(x, y, z))**2

peso = volumen * suma_peso / N_steps
x = volumen * suma_x / N_steps
y = volumen * suma_y / N_steps
z = volumen * suma_z / N_steps
error_peso = volumen * np.sqrt((varianza_peso / N_steps -
                                (suma_peso / N_steps)**2) / N_steps)
error_x = volumen * np.sqrt((varianza_x / N_steps -
                             (suma_x / N_steps)**2) / N_steps)
error_y = volumen * np.sqrt((varianza_y / N_steps -
                             (suma_y / N_steps)**2) / N_steps)
error_z = volumen * np.sqrt((varianza_z / N_steps -
                             (suma_z / N_steps)**2) / N_steps)
X_cm = x / peso
Y_cm = y / peso
Z_cm = z / peso

error_x_total = X_cm * (error_peso / peso + error_x / x)
error_y_total = Y_cm * (error_peso / peso + error_y / y)
error_z_total = Z_cm * (error_peso / peso + error_z / z)


print("r_cm=(%s,%s,%s)" % (X_cm, Y_cm, Z_cm))
print("Eror_cm=(%s,%s,%s)" % (error_x_total, error_y_total, error_x_total))


# plot de las superficies
plt.figure(1)
angle = np.linspace(0, 2 * np.pi, 50)
theta, phi = np.meshgrid(angle, angle)
r, R = 1., 3.
X_toro = (R + r * np.cos(phi)) * np.cos(theta)
Y_toro = (R + r * np.cos(phi)) * np.sin(theta)
Z_toro = r * np.sin(phi)
for i in range(50):
    for j in range(50):
        if X_toro[i][j] < 1 or X_toro[i][j] > 3:
            X_toro[i][j] = np.nan
        if Y_toro[i][j] < -4 or Y_toro[i][j] > 4:
            Y_toro[i][j] = np.nan
        if Z_toro[i][j] < -1 or Z_toro[i][j] > 1:
            z_toro[i][j] = np.nan


# Display the mesh
plt.clf()
fig1 = plt.figure(1)
ax = fig1.gca(projection='3d')
ax.set_xlim3d(-4, 4)
ax.set_ylim3d(-4, 4)
ax.set_zlim3d(-4, 4)
ax.plot_wireframe(X_toro, Y_toro, Z_toro, color='k', rstride=1, cstride=1)
ax.plot([X_cm], [Y_cm], [Z_cm], markerfacecolor='r', markeredgecolor='r',
        marker='o', markersize=5, alpha=0.6)
ax.set_xlabel('x', color='k')
ax.set_ylabel('y', color='k')
ax.set_zlabel('z', color='k')
plt.savefig("Totoro.eps")
plt.show()
plt.draw()

fig2 = plt.figure(2)
axes = plt.gca()
axes.set_xlim([-4, 4])
axes.set_ylim([1, 3])
plt.axes().set_aspect('equal', 'datalim')
plt.plot(Y_toro, X_toro, 'k')
plt.plot([Y_cm], [X_cm], markerfacecolor='r', markeredgecolor='r',
         marker='o', markersize=5, alpha=0.6)
plt.xlabel('Y', color='k')
plt.ylabel('X', color='k')
plt.savefig("XY.eps")
plt.show()
plt.draw()

fig3 = plt.figure(3)
axes = plt.gca()
axes.set_xlim([1, 3])
axes.set_ylim([-1, 1])
plt.axes().set_aspect('equal', 'datalim')
plt.plot(X_toro, Z_toro, 'k')
plt.plot([X_cm], [Z_cm], markerfacecolor='r', markeredgecolor='r',
         marker='o', markersize=5, alpha=0.6)
plt.xlabel('X', color='k')
plt.ylabel('Z', color='k')
plt.savefig("XZ.eps")
plt.show()
plt.draw()

fig4 = plt.figure(4)
axes = plt.gca()
axes.set_xlim([-4, 4])
axes.set_ylim([-1, 1])
plt.axes().set_aspect('equal', 'datalim')
plt.plot(Y_toro, Z_toro, 'k')
plt.plot([Y_cm], [Z_cm], markerfacecolor='r', markeredgecolor='r',
         marker='o', markersize=5, alpha=0.6)
plt.xlabel('x', color='k')
plt.ylabel('y', color='k')
plt.savefig("YZ.eps")
plt.show()
plt.draw()

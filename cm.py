#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pdb

''' script que determina la posici?n del centro de masa de un s?lido descrito
por la intersecci?n de un cilindro y un toro dados por:
Toro : z ** 2 + (np.sqrt(x ** 2 + y ** 2) - 3) ** 2 <= 1
Cilindro: (x - 2) ** 2 + z ** 2 <= 1
Densidad: 0.5 * (x ** 2 + y ** 2 + z ** 2)
usando m?todo de montecarlo'''


def esta_en_cilindro(x, y, z):
    '''Devuelve true si el punto entregado se encuentra dentro del
    cilindro'''
    if ((x - 2) ** 2 + z ** 2 <= 1):
        return True
    return False


def esta_en_toro(x, y, z):
    '''Devuelve true si el punto x, y, z est? dentro del toro'''
    if (z ** 2 + (np.sqrt(x ** 2 + y ** 2) - 3) ** 2 <= 1):
        return True
    return False


def densidad(x, y, z):
    '''recibe las coordenadas de un punto, y devuelve la densidad del s?lido
    en esepunto'''
    return 0.5 * (x ** 2 + y ** 2 + z ** 2)


def generar_random_cilindro():
    ''' recibe los l?mites de X Y en los que se define el volumen, devuelve
    una coordenada random que pertenece al volumen.
    los l?mites de la coordenada z se calcula con los de la coordenada x
    para que el punto se encuentre en el cilindro'''
    X = [1, 3]
    Y = [-4, 4]
    x = np.random.uniform(X[0], X[1])
    Z_0 = -np.sqrt(1 - (x - 2) ** 2)
    Z_1 = np.sqrt(1 - (x - 2) ** 2)
    y = np.random.uniform(Y[0], Y[1])
    z = np.random.uniform(Z_0, Z_1)
    return [x, y, z]


def mostrar(m, x, y, z):
    '''histograma para los valores de masa total, y coordenadas del
    centro de masa'''
    mm = np.mean(m)
    xx = np.mean(x)
    yy = np.mean(y)
    zz = np.mean(z)
    fig, ax = plt.subplots()
    num_bins = 20
    n, bins, patches = ax.hist(m, num_bins, normed=1, facecolor='green',
                               alpha=0.5)
    ax.axvline(x=mm, color='blue', linestyle='solid',
               label='masa total promedio')
    ax.set_xlabel('Masa total [unidades de masa]')
    ax.set_ylabel('# veces obtenido / # Total')
    ax.set_title(r'Histograma de la masa total calculada')
    plt.savefig("masa.jpg")
    plt.legend()

    fig2, ax2 = plt.subplots()
    n2, bins2, patches2 = ax2.hist(x, num_bins, normed=1,
                                   facecolor='y', alpha=0.5)
    ax2.axvline(x=xx, color='blue', linestyle='solid',
                label='X promedio')
    plt.legend()
    ax2.set_xlabel('coordenda X [unidades de distancia]')
    ax2.set_ylabel('# veces obtenido / # Total')
    ax2.set_title(r'Histograma las coordendas x del centro de masa')
    plt.savefig("X.jpg")

    fig3, ax3 = plt.subplots()
    n3, bins3, patches3 = ax3.hist(z, num_bins, normed=1,
                                   facecolor='red', alpha=0.5)
    ax3.axvline(x=zz, color='blue', linestyle='solid',
                label='Z promedio')
    plt.legend()
    ax3.set_xlabel('coordenda Z [unidades de distancia]')
    ax3.set_ylabel('# veces obtenido / # Total')
    ax3.set_title(r'Histograma las coordendas z del centro de masa')
    plt.savefig("Z.jpg")

    fig4, ax4 = plt.subplots()
    n4, bins4, patches4 = ax4.hist(y, num_bins, normed=1,
                                   facecolor='blue', alpha=0.5)
    ax4.axvline(x=yy, color='red', linestyle='solid',
                label='Y promedio')
    plt.legend()
    ax4.set_xlabel('coordenda "Y" [unidades de distancia]')
    ax4.set_ylabel('# veces obtenido / # Total')
    ax4.set_title(r'Histograma las coordendas y del centro de masa')
    plt.savefig("Y.jpg")

    plt.show()


SEMILLA = 3
np.random.seed(int(SEMILLA))
NRUNS = 100
N = 10000  # numero de puntos a tomar
VOL = np.pi * 8
masas = np.zeros(NRUNS)
CM_X = np.zeros(NRUNS)
CM_Y = np.zeros(NRUNS)
CM_Z = np.zeros(NRUNS)

for j in range(NRUNS):
    sum_den = 0
    sum_den_x = 0
    sum_den_y = 0
    sum_den_z = 0
    for i in range(N):
        punto = generar_random_cilindro()
        x, y, z = punto[0], punto[1], punto[2]
        if esta_en_toro(x, y, z):
            sum_den += densidad(x, y, z)
            sum_den_x += x * densidad(x, y, z)
            sum_den_y += y * densidad(x, y, z)
            sum_den_z += z * densidad(x, y, z)

    masa = VOL * sum_den / N
    cm_x = (VOL * sum_den_x / N) / masa
    cm_y = (VOL * sum_den_y / N) / masa
    cm_z = (VOL * sum_den_z / N) / masa
    masas[j] = masa
    CM_X[j] = cm_x
    CM_Y[j] = cm_y
    CM_Z[j] = cm_z

mostrar(masas, CM_X, CM_Y, CM_Z)

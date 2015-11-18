#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################################################################
#                                TAREA 8                                    #
#############################################################################

'''
Universidad de Chile
Facultad de Ciencias Fisicas y Matematicas
Departamento de Fisica
FI3104 Metodos Numericos para la Ciencia y la Ingenieria
Semestre Primavera 2015

Nicolas Troncoso Kurtovic
'''

import matplotlib.pyplot as p
import numpy as np
from scipy import integrate as sci

#############################################################################
#                                                                           #
#############################################################################


def w(x):
    '''
    Funcion distribucion. La normalizacion fue calculada entre -100 y 100.
    '''
    a = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-(x + 1.5)**2 / 0.5)
    norm = 13.2515587081
    return a / norm


def un_paso_metropolis(w, xn, d):
    '''
    Un paso segun algoritmo de Metropolis.
    - Input: (funcion, semilla, distancia).
    - Output: xn o xp, segun criterio metropolis.
    En base a un 'xn' dado evalua un 'xp' nuevo generado de manera random
    ubicado en un conjunto [xn - d, xn + d]. Si el xp cumple el criterio de
    Metropolis, retorna xp, en caso contrario retorna xn.
    '''
    r = np.random.uniform(-1., 1.)
    xp = xn + d * r
    filtro = np.random.uniform(0., 1.)
    if w(xp) / w(xn) > filtro:
        return xp
    else:
        return xn


def generador(w, xn, N, d):
    '''
    Generador de funcion distribucion.
    - Input: (funcion, xn semilla, Numero de bins, distancia pasos).
    - Output: Arreglo 'y' distribuido segun w, porcentaje de pasos aceptados.
    '''
    y = np.zeros(N)
    # Guardar la primera semilla
    y[0] = np.copy(xn)
    # Contador de aceptados y rechazados respectivamente
    j = 0.
    k = 0.
    for i in range(len(y)-1):
        y[i+1] = un_paso_metropolis(w, y[i], d)
        if y[i+1] == y[i]:
            k += 1.
        else:
            j += 1.
    porcentaje = 100. * j / (j + k)
    return y, porcentaje


def calculador_d(dmin, dmax, N):
    '''
    Porcentaje de aceptados en funcion de la distancia de los pasos.
    - Input: (dmin, dmax, Numero pasos)
    - Output: Arreglo de distancias 'D', Arreglo de porcentajes 'P'.
    '''
    D = np.linspace(dmin, dmax, N)
    P = np.zeros(len(D))
    for i in range(len(D)):
        y2, porcentaje = generador(w, 0., 10**5, D[i])
        P[i] = np.copy(porcentaje)
    return D, P


def calculador_error(w, N, n, l, d):
    '''
    Calculador de error en el histograma.
    - Input: (funcion, N=numeros, n=iteraciones, largo hist, distancia).
    - Output: Arreglo 'S' de desviaciones estandar en cada bin.
    '''
    Y = np.zeros([N, n])
    for i in range(n):
        xn = np.random.uniform(-2., 2.)
        Y[:, i], porcentaje = generador(w, xn, N, d)
    H = np.zeros([l-1, n])
    for i in range(n):
        num, bins, patches = p.hist(Y[:, i], normed=1, bins=np.linspace(-10., 10., l))
        H[:, i] = num
    S = np.zeros(l-1)
    for i in range(len(S)):
        S[i] = np.std(H[i, :])
    return bins, S


def guardar_archivo(x, y, nombre):
    '''
    Crea un archivo 'nombre.dat' con dos columnas. No lleva header.
    '''
    arch = open(nombre + '.dat', 'w')
    for i in range(len(x)):
        arch.write(str(x[i])+' '+str(y[i])+'\n')
    arch.close()


#############################################################################
#                                                                           #
#############################################################################


# Semilla
np.random.seed(251093)

'''
# Encontrar d optimo. Se encuentra d = 3.96
D, P = calculador_d(3., 5., 50)
p.plot(D, P, '.')
p.xlabel("Distancia pasos $d$")
p.ylabel("Porcentaje aceptados")
p.show()
'''

# Vectores a utilizar
x1 = np.linspace(-10., 10., 10**6)
y1 = w(x1)

y2, porcentaje = generador(w, 0., 10**6, 3.96)

'''
# Integral para calcular normalizacion
integral = sci.trapz(y1, x=x1)
print integral


# Ploteo
fig1 = p.figure()
fig1.clf()
m, bins, patches = p.hist(y2, normed=1, bins=10**2)
p.plot(x1, y1, 'r')
p.xlabel("$x$")
p.ylabel("$W(x)$")
p.show()
'''

# calculador_error(w, N, n, l, d)
#bins, S = calculador_error(w, 10**6, 100, 1000, 3.96)
#x2 = bins[:-1]

#guardar_archivo(bins, S, 'std')
archivo = np.loadtxt('std.dat')  # Se abre el archivo

x = archivo[:, 0]
y = archivo[:, 1]
#y = y[:-1]

num, bins, patches = p.hist(y2, normed=1, bins=np.linspace(-10., 10., 100))
p.plot(x1, y1, 'r-')
p.show()

fig2 = p.figure(2)
fig2.clf()
p.plot(x, y, '*')
p.plot(x1, y1)
p.xlabel("$x$")
p.ylabel("$std(x)$")
p.axis([-10., 10., -0.01, 0.3])
p.show()

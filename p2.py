'''
Este script genera una muestra de 10 millones de puntos con una distribucion
muy similar a una dada:
(w(x)=3.5 * exp(-(x - 3)^2 / 3) + 2. * exp(-2 * (x + 1.5)^2))
Utilizando el algoritmo de metrópolis.
Finalmente crea un histograma de la muestra con 50 bins y plotea encima a la
funcion w(x).
'''
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapz
import time
start_time = time.time()


def w(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion


def w_normalizado(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion / integral


# No es necesario ocupar w_normalizado
def metropolis(w, xn, delta):
    r = np.random.uniform(-1., 1.)
    xp = xn + delta * r
    gamma = np.random.uniform(0., 1.)
    if w(xp) / w(xn) > gamma:
        return xp
    else:
        return xn


def xn_mas_1(w, xn, N, delta):
    xn_mas_1 = np.zeros(N)
    xn_mas_1[0] = np.copy(xn)
    aceptados = 0.
    rechazados = 0.
    for i in range(len(xn_mas_1)-1):
        xn_mas_1[i+1] = metropolis(w, xn_mas_1[i], delta)
        if xn_mas_1[i+1] == xn_mas_1[i]:
            rechazados += 1.
        else:
            aceptados += 1.
    porcentaje_aceptados = 100.0 * aceptados / (aceptados + rechazados)
    return xn_mas_1, porcentaje_aceptados

# Se escoge semilla
np.random.seed(212)

# Se estima delta
n = 30
d_posibles = np.linspace(1., 10., n)
porcentajes = np.zeros(n)
for i in range(n):
    xn1, porcentaje = xn_mas_1(w, 0., 1e3, d_posibles[i])
    porcentajes[i] = np.copy(porcentaje)

# Se grafica deltas posibles vs porcentaje aceptados,
# se estima d optimo = 3.79
fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
plt.plot(d_posibles, porcentajes, '-o', color='r')
ax2.set_xlabel("Valor posible de $\delta$")
ax2.set_ylabel("Porcentaje de veces aceptado")
plt.axhline(y=50, color='g')
plt.axvline(x=3.79, linewidth=1, color='0')
plt.show()
plt.draw()
plt.savefig('d_vs_porcentaje.png')

# Se grafica W(x) normalizado
x = np.linspace(-10., 10., 1e5)
integral = trapz(w(x), x=x)
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111)
plt.plot(x, w_normalizado(x), color='r', label="Distribucion deseada")
ax.set_xlabel("x")
ax.set_ylabel("W(x)")

# Se grafica histograma de f_distribucion_w
f_distribucion_w, porcentaje_final = xn_mas_1(w, 0., 10**7, 3.79)
bins_escogido = np.linspace(-10, 10, 51)
n, bins, patches = plt.hist(f_distribucion_w, bins_escogido, normed=1,
                            facecolor='g', alpha=0.5)
print porcentaje_final

plt.legend()
plt.show()
plt.draw()
plt.savefig('w(x).png')
print("--- %s seconds ---" % (time.time() - start_time))

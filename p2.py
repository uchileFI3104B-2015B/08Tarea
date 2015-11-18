'''
Este script genera una muestra aleatoria según la distribucion W(x) usando
el método de metrópolis. Además determina el delta eficiente para que trabaje
el método aceptando alrededor del 50% de las proposiciones.
Finalmente grafica W(x) normalizada y el histograma de la muestra aleatoria.
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(83819)


def W(x):
    return (3.5 * np.exp(- (x - 3) ** 2 / 3.) +
            2 * np.exp(- (x + 1.5) ** 2 / 0.5))


def W_norm(x, norma):
    # Distribucion normalizada
    W = 3.5 * np.exp(- (x - 3) ** 2 / 3.) + 2 * np.exp(- (x + 1.5) ** 2 / 0.5)
    W_norm = W / norma
    return W_norm


def metropolis(w, xn, delta):
    # Algoritmo del método Metrópolis
    r = np.random.uniform(-1, 1)
    xp = xn + delta * r
    criterio = np.random.uniform(0, 1)
    if w(xp) / w(xn) > criterio:
        return xp
    else:
        return xn


def calcula_porcentajes(delta, N, w, xn):
    # Calcula el porcentaje de aceptacion para un delta, dado un xn
    xn_1 = np.zeros(N)
    xn_1[0] = xn
    acepta = 0.
    rechaza = 0.
    for i in range(len(xn_1)-1):
        xn_1[i+1] = metropolis(w, xn_1[i], delta)
        if xn_1[i+1] == xn_1[i]:
            rechaza += 1.
        else:
            acepta += 1.
    porcentaje_acepta = 100.0 * acepta / (acepta + rechaza)
    return porcentaje_acepta, xn_1


# Main

# Setup
# n servirá para hacer la particion para los delta posibles
n = 50
# N servirá para ver cuántos valores de la muestra deseo
N = 100

xn_inicial = 0

# Calcula la integral de w(x)
x_integral = np.linspace(-10, 10, 10000)
norma = np.trapz(W(x_integral), x_integral)

# Calcula Delta eficiente
delta_posibles = np.linspace(1., 10., n)
porcentaje = np.zeros(n)
for i in range(n):
    porcentajes, xn1 = calcula_porcentajes(delta_posibles[i], N, W, xn_inicial)
    porcentaje[i] = np.copy(porcentajes)

for i in range(n):
    if porcentaje[i] >= 49 and porcentaje[i] <= 51:
        d = delta_posibles[i]
        break

# Graficar W(x) normalizado
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111)
plt.plot(x_integral, W_norm(x_integral, norma),
         label='Distribucion W(x) normalizada')
ax.set_xlabel("x")
ax.set_ylabel("W(x)")
ax.set_title("Grafico W(x) normalizada e histograma de variables aleatorias")

# Se grafica histograma para la distribucion encontrada
porcentaje_hist, xn_1_hist = calcula_porcentajes(d, 1e7, W, xn_inicial)
n, bins, patches = plt.hist(xn_1_hist, bins=100, normed=1)

plt.legend()
plt.show()
plt.draw()

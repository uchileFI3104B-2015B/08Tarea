'''
Este script genera una muestra aleatoria de numeros dada por la distribucion
w(x) = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
utilizando el metodo de metropolis y los muestra en un grafico tipo histograma.
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


# Designamos la semilla
np.random.seed(1994)


def w(x):
    # Distribucion sin normalizar
    return 3.5 * np.exp(-(x - 3.) ** 2 / 3.) + 2. * np.exp(-2 * (x + 1.5) ** 2)


def W(x):
    # Distribucion normalizada
    return w(x) / norma


def metropolis(w, xn, d):
    # Algoritmo de metropolis
    r = np.random.uniform(-1., 1.)
    xp = xn + d * r
    c = np.random.uniform(0., 1.)
    if (w(xp) / w(xn)) > c:
        return xp
    else:
        return xn


def porcentaje_acepta(w, xn, N, d):
    # Entrega valores de porcentaje aceptados para cada delta
    xn_mas_1 = np.zeros(N)
    xn_mas_1[0] = xn
    acepto = 0.
    rechazo = 0.
    for i in range(len(xn_mas_1) - 1):
        xn_mas_1[i+1] = metropolis(w, xn_mas_1[i], d)
        if xn_mas_1[i+1] == xn_mas_1[i]:
            rechazo += 1.
        else:
            acepto += 1.
    porcentaje = 100.0 * acepto / (acepto + rechazo)
    return porcentaje, xn_mas_1


# Main
# Set up

# Inicializo valores
N = 100
n = 30
xn_0 = 0
d_posible = np.linspace(1., 10., n)
porcentaje = np.zeros(n)

# Iteramos para mostrar los porcentajes aceptados
for i in range(n):
    porcentajes, xn_mas_1 = porcentaje_acepta(w, xn_0, N, d_posible[i])
    porcentaje[i] = np.copy(porcentajes)

# Establecemos condicion de porcentaje = 50% (aprox) para estimar el delta
for i in range(n):
    if porcentaje[i] >= 49 and porcentaje[i] <= 51:
        d = d_posible[i]
        break

print d  # Se estimó d=4.72


# Calculo la integral de w para normalizar
x_int = np.linspace(-10, 10, 1000)
norma = np.trapz(w(x_int), x_int)

# Plot W(x) (normalizado)
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111)
plt.plot(x_int, W(x_int), color='r', label="Distribucion deseada")
ax.set_xlabel("x")
ax.set_ylabel("W(x)")

# Plot Histograma
porcentaje_hist, xn_1_hist = porcentaje_acepta(w, xn_0, 1e7, d)
n, bins, patches = plt.hist(xn_1_hist, bins=100, normed=1)

plt.legend()
plt.savefig('w_x.png')
plt.show()
plt.draw()

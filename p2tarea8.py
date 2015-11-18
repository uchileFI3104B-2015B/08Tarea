'''
Este script genera una muestra de puntos con distribución
W(x) = (3.5 * np.exp(-(x - 2)**2 / 3) + 2 * np.exp(-(x + 1.5)**2 / 0.5))
mediante el algoritmo de Metropolis.
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(456)

def W(x):
    w = (3.5 * np.exp(-(x - 2)**2 / 3) +
         2 * np.exp(-(x + 1.5)**2 / 0.5))
    return w

def prueba(x):
    r = np.random.uniform(-1, 1)
    xp = x + r * delta
    return xp

# Main
# Setup

delta = 4.5
N = 10000000
N_aceptados = 0
norma = np.sqrt(np.pi) * (3.5 * np.sqrt(3) + 2 * np.sqrt(0.5))
x = np.zeros(N + 1)

# Algoritmo de Metropolis
for i in range(N):
    h = np.random.uniform(0, 1)
    xp = prueba(x[i])
    if (W(xp) / W(x[i])) > h:
        x[i+1] = xp
        N_aceptados += 1
    else:
        x[i+1] = x[i]

print(N_aceptados)

# Plot
plt.clf()
plt.figure(1)
x_values = np.linspace(-10, 10, 1000)
plt.hist(x, bins=100, range=[-10, 10], normed=True, color='c', label="Distribucion obtenida")
plt.plot(x_values, W(x_values)/norma, color='r', linewidth=2, label="Distribucion deseada")
plt.xlim([-10, 10])
plt.ylim([0, 0.3])
plt.xlabel('$x$')
plt.ylabel('$W(x)$')
plt.legend(loc='upper left')
plt.savefig('grafico1.png')
plt.show()

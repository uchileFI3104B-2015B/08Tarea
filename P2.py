import numpy as np
import matplotlib.pyplot as plt


def next_point(x_n, dist):
    '''
    Calcula punto x_p usando la ecuacion:
    x_p = x_n + U(-1, 1) * dist, donde U es una distr. uniforme
    Entradas
    x_n: punto actual
    dist: largo del paso
    Salidas
    x_p: punto siguiente propuesto
    '''
    return x_n + dist * np.random.uniform(-1.0, 1.0)

def distr_W(x):
    ''' Retorna el valor de la distribucion
    no normalizada W(x) en el punto x '''
    return 3.5 * np.exp(-(x - 3)**2 / 3) + 2 * np.exp(-(x + 1.5)**2 / 0.5)

''' Algoritmo de Metropolis '''

np.random.seed(1357)

N = 1e6  # Cantidad de muestras
dist = 2.0  # Tamano de paso del algoritmo
x_0 = 0.0  # Posicion inicial
sample = []  # Almacena puntos aceptados
aprov = 0  # Almacena cantidad de puntos aprobados

# Se inician interaciones
x_n = x_0
j = 0
while j < N:

    x_p = next_point(x_n, dist)
    test_val = distr_W(x_p) / distr_W(x_n)

    # Se evita calcular distr. uniforme si test > 1
    if test_val > 1 or test_val > np.random.uniform(0.0, 1.0):
        x_n = x_p
        aprov += 1

    sample.append(x_n)
    j += 1

print('Procentaje Aprobados = ' + str(aprov/N * 100))

''' Graficos '''

# Distribucion sin normalizar
x_plt = np.arange(-4.0, 7.0, 0.1)
W = distr_W(x_plt)
fig1 = plt.figure()
plt.plot(x_plt, W)

# Distribucion normalizada
x = np.arange(-70.0, 100.0, 0.1)
W = distr_W(x)
area = abs(np.trapz(x,W))
W_norm = W / area
fig2 = plt.figure()
plt.plot(x, W_norm)
plt.hist(sample, normed = 1, bins = 40)

plt.show()

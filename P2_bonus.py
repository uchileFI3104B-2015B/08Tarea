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

def algoritmo_metropolis(seed, N, dist):
    ''' Ejecuta el algoritmo de Metropolis
    con una semilla determinada por el usuario.
    Retorna las muestras obtenidas '''

    np.random.seed(1357)

N = 1e7  # Cantidad de muestras
dist = 2  # Tamano de paso del algoritmo
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

''' Graficos '''

# Se normaliza distribucion usando area
x = np.arange(-70.0, 100.0, 0.1)
W = distr_W(x)
area = abs(np.trapz(x,W))
W_norm = W / area

# Creamos histograma con bins fijos
bins = np.arange(-6, 10, 0.1)
hist_val = np.histogram(sample, bins)
fig2 = plt.figure()
plt.plot(x, W_norm, label = 'W(x) Normalizada')
plt.hist(sample, normed = 1, bins = bins, label = 'Histograma Muestras')
plt.rc('text', usetex=True)
str_title = "Distribucion W(x) normalizada vs Histograma de $10^7$ Muestras \n\
            obtenidas con Algoritmo de Metropolis"
plt.title(str_title, y=1.02)
plt.ylabel('Frecuencia', size=14)
plt.xlabel('x', size=14)
plt.grid()
plt.legend(loc=2)

plt.show()

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
# END of next_point


def distr_W(x):
    ''' Retorna el valor de la distribucion
    no normalizada W(x) en el punto x '''
    return 3.5 * np.exp(-(x - 3)**2 / 3) + 2 * np.exp(-(x + 1.5)**2 / 0.5)
# END of distr_W


def algoritmo_metropolis(N, x_0, dist):
    ''' Ejecuta el algoritmo de Metropolis
    N: Numero de muestras
    x_0: Posicion inicial
    dist: distancia maxima de paso
    Retorna arreglo con las muestras generadas '''

    sample = []  # Almacena puntos aceptados
    # Se inician interaciones
    x_n = x_0
    j = 0
    while j < N:

        x_p = next_point(x_n, dist)
        test_val = distr_W(x_p) / distr_W(x_n)

        # Se evita calcular distr. uniforme si test > 1
        if test_val > 1 or test_val > np.random.uniform(0.0, 1.0):
            x_n = x_p

        sample.append(x_n)
        j += 1

    return sample
# END of algoritmo_metropolis

''' Algoritmo de Metropolis '''

N_iter = 100  # Numero de iteraciones
N = 1e5  # Cantidad de muestras por iteracion
dist = 2  # Tamano de paso del algoritmo
samples = []  # Almacena muestras de cada iteracion
histogramas = []  # Almacena histogramas
np.random.seed(1234)

'''Generacion de 100 muestras del algoritmo'''
for n in range(N_iter):
    ''' Para cada iteracion se crea nueva posicion inicial
    y distancia maxima de paso'''
    x_0 = np.random.uniform(-1.0, 1.0)
    d = np.random.uniform(0.5, 3)

    new_sample = algoritmo_metropolis(N, x_0, dist)
    samples.append(new_sample)

''' Calculo del error '''
for n in range(N_iter):
    bins = np.arange(-6, 10, 0.1)
    hist, bin_edges = np.histogram(samples[n], bins=bins)
    histogramas.append(hist)

''' Calculo de la media para cada barra '''

mean_samples = np.mean(samples, axis=0)
mean_hist = np.mean(histogramas, axis=0)
std_hist = np.std(histogramas, axis=0)
print(histogramas)

''' Normalizar '''
norm = np.sum(mean_hist * 0.1)
mean_hist = mean_hist / norm
std_hist = std_hist / norm


''' Graficos '''

# Se normaliza distribucion usando area
x = np.arange(-70.0, 100.0, 0.1)
W = distr_W(x)
area = abs(np.trapz(x, W))
W_norm = W / area

# Posicion de las barras de error
bin_centers = 0.5*(bins[1:] + bins[:-1])
width = 0.1
# Se grafica histograma medio con barras de error
fig2 = plt.figure()
plt.plot(x, W_norm, label='W(x) Normalizada')
plt.bar(bin_centers, mean_hist, width=width, color='c', yerr=std_hist,
        error_kw=dict(elinewidth=2, ecolor='black'), label='Hist. promedio\
        con error')

plt.rc('text', usetex=True)
str_title = "Distribucion W(x) normalizada vs Histograma de Muestras \n\
            Error estimado con 100 series de $10^5$ muestras"
plt.title(str_title, y=1.02)
plt.ylabel('Frecuencia', size=14)
plt.xlabel('x', size=14)
plt.grid()
plt.xlim([-3.5, 8])
plt.ylim([0, 0.29])
plt.legend(loc=2)

plt.show()
plt.draw()

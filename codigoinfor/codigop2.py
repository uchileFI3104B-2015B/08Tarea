import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.integrate import quad
''' script que resuelve la parte 2 ocupando Metropolis y monte carlo en la
funcion de W(x)'''

np.random.seed(93)


def W(x):
    return 3.5 * np.exp(-(x - 3)**2 / 3) + 2 * np.exp(-(x + 1.5)**2 / 0.5)


# Primera forma de calcular la integral
I = quad(W, -10, 10)
# Otra forma de calcular integral
x3 = np.linspace(-10, 10, 10**6)
i = scipy.trapz(W(x3), x=x3)


def paso_metropolis(W, xn, d):
    ''' Algoritmo de Metropolis '''

    r = np.random.uniform(-1, 1)
    xp = xn + d * r
    m = np.random.uniform(0, 1)
    if W(xp) / W(xn) > m:
        # Acepta xp
        return xp
    else:
        # Rechaza xp
        return xn


def create(W, xn, N, d):
    '''
    Retorna arreglo de x segun W con el porcentaje de pasos aceptados
    '''
    x = np.zeros(N)
    # first semilla
    x[0] = xn
    # Contador de aceptados y rechazados respectivamente
    a = 0
    r = 0
    for i in range(N-1):
        x[i+1] = paso_metropolis(W, x[i], d)
        if x[i+1] == x[i]:
            r += 1.
        else:
            a += 1.
    porcentaje = 100 * a / (a + r)

    return x, porcentaje


def calc_d(dmin, dmax, N_pasos):
    D = np.linspace(dmin, dmax, N_pasos)
    P = np.zeros(N_pasos)
    for i in range(N_pasos):
        P[i] = create(W, 0, 10**5, D[i])[1]

    return D, P

# d optimo.Tomamos como dmin=3 y dmax=5.Luego,se encuentra d=3.96
D, P = calc_d(3, 5, 50)
plt.figure(1)
plt.plot(D, P, '.', color='g')
plt.title('Grafico representatito del valor de d a tomar')
plt.xlabel("Distancia pasos $d$")
plt.ylabel("Porcentaje de aceptados")
plt.savefig('calculod.png')

# tomamos xn=0, donde se concentra cierta cantidad de la distribucion
d = 3.96
x2, porcentaje = create(W, 0, 10**6, 1)
# efectivamente como se pedia, se aceptan mas del 50%
# (50.15850158501585) de los v.prop
# Con 10 millones se demora como 5 min en graficar


# Grafico sin error para bins
plt.figure(3)
plt.plot(x3, W(x3)/i, 'r', label='Distribucion de probabilidad normalizada')
plt.hist(x2, normed=1, bins=100, color='g', fill=True, label='Histograma')
# si no esta normalizado , osea false, quedan valores en eje y muy elevados
plt.xlabel('Variable aleatoria x')
plt.ylabel('Distribucion W(x) con Histograma ')
plt.legend(loc='best')
plt.title('Distribucion W(x) agregando algoritmo Monte Carlo')
plt.savefig('Distribucionxn0d1.png')


''' PARTE EXTRA '''

'''Volvemos al codigo metropolis para ocupar en 100 histogramas con semilla.
    diferencia es que esta vez retorna resultados para los histogramas(bins)'''
N = 10**4
# 10**7 y 6 era demasiado tiempo (horas)


def calc_hist_metropolis(semilla):
    np.random.seed(semilla)
    x = np.zeros(N + 1)
    i = 0
    while i < N:
        r = np.random.uniform(-1, 1)
        xp = x[i] + r*d
        m = np.random.uniform(0, 1)
        if W(xp) / W(x[i]) > m:
            x[i+1] = xp
        else:
            x[i+1] = x[i]
        i += 1
    return np.histogram(x, bins=100, range=(-5, 10), normed=True)


''' 100 histogramas '''

x = np.linspace(-5, 10, 10**4)
h_result = np.zeros((100, 100))
for n in range(100):
    hist_now = calc_hist_metropolis(n)
    for i in range(100):
        h_result[i][n] = hist_now[0][i]

bins = hist_now[1]  # fijo,valores entre -5 y 10 ,en este caso, saltando 0.15
h_std = np.zeros(100)
h_m = np.zeros(100)

for i in range(100):
    h_std[i] = np.std(h_result[i])
    h_m[i] = np.mean(h_result[i])


# Grafico parte extra(con error para bins)
plt.clf()
plt.figure(2)
center = (bins[:-1] + bins[1:]) / 2
# inicio y final respectivamente
plt.bar(center, h_m, align='center', color='o', width=0.15, label="Histograma")

plt.plot(x, W(x)/i, color='red', linewidth=1.6, label="Distribucion dada")

plt.errorbar(bins[0:100] + 0.075, h_m, yerr=h_std, fmt='.', color='black',
             label="Barra de error (desviacion estandar)", linewidth=1.5)

plt.ylim([0, 0.45])
plt.xlim([-5, 10])
plt.title('Distribucion W(x) con error asociado')
plt.xlabel(' Variable aleatoria x')
plt.legend(loc='best')
plt.savefig('Errorbar.png')


plt.show()

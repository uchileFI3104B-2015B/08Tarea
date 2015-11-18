from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

np.random.seed(1911)


def w(x):
    '''
    Funcion distribucion sin normalizar
    '''
    return (3.5 * np.exp(-(x - 3.)**2 / 3.) + 2 * np.exp(-(x + 1.5)**2 / 0.5))


def normalizacion(x_i, x_f):
    '''
    Entre el punto inicial y final se calcula la normalizacion
    para 5000 puntos por medio de una integracion numerica dada
    por el metodo trapezoidal incluida en la libreria scipy.
    '''
    x = np.linspace(x_i, x_f, 5000)
    return integrate.trapz(w(x), x=x)


def metropolis(x_n, d):
    '''
    Un paso segun Metropolis. Con un valor de x_n, evalua
    si un nuevo x_p (generado aleatoriamente) cumple con el
    criterio de metropolis dada la funcion w(x).
    '''
    x_p = lambda: x_n + d * r  # Distribucion proposicion

    r = np.random.uniform(-1, 1)
    N = np.random.uniform(0., 1.)

    if w(x_p()) / w(x_n) > N:
        return x_p()
    else:
        return x_n



def delta_optimo(d_min, d_max, prueba):
    '''
    Determina delta tal que se acepte el 50% de las
    pruebas (o se rechace) segun metropolis
    '''
    deltas = np.linspace(d_min, d_max, prueba)
    datos = np.zeros(prueba)
    Porcentaje = 0
    n = 0

    while np.fabs(Porcentaje - 50.) >= 0.01:
        win = 0
        fail = 0
        datos[0] = np.random.uniform(-10., 10.)

        for i in range(0, prueba - 1):
            datos[i+1] = metropolis(datos[i], deltas[n])
            if datos[i+1] == datos[i]:
                win += 1
            else:
                fail += 1

        Porcentaje = 100 * win / prueba
        n += 1

    return deltas[n]

#  Setup
step = 10**7
x = np.linspace(-10., 10., step)
Datos = np.zeros(step)
Datos[0] = np.random.uniform(-10., 10.)
Dist = np.zeros(step)

#  Main
delta = delta_optimo(-10, 10, 50)
norm = normalizacion(-10, 10)
print 'Normalizacion =', norm
print 'Delta optimo =', delta

for i in range(1, step):
    Datos[i] = metropolis(Datos[i-1], delta)
    Dist[i] = w(x[i]) / norm

# Segunda posicion = numero de barritas, alpha = opacidad
n, bins, patches = plt.hist(Datos, 75, normed=1, facecolor='purple', alpha=0.4, label='Histograma')
plt.plot(x, Dist, 'g', label='Distribucion creada')
plt.xlabel("$x$")
plt.ylabel("$W(x)$")
plt.legend()
plt.show()

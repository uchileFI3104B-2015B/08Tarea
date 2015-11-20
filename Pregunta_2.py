"""
Sript que utiliza el algoritmo de metropolis para obtener aproximacion de la
densidad de probabilidad W(x), la cual corresponde a:
3.5*exp(-(x-3^*2/3) + 2*exp(-(x+1.5)^2/0.5)

"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(55)


def W(x):
    """
    Retorna el valor de la funcion de densidad W en el punto x
    """
    return 3.5*np.exp(-(x-3)**2/3) + 2*np.exp(-(x+1.5)**2/0.5)


N_muestra = 1e7
delta = 4
x_muestra = np.zeros(N_muestra + 1)
x_0 = 0
x_muestra[0] = x_0

aceptados = 0
no_aceptados = 0

i = 0
while i < N_muestra:
    r = np.random.uniform(-1, 1)
    u = np.random.uniform(0, 1)
    xp = x_muestra[i] + delta*r
    if W(xp)/W(x_muestra[i]) > u:
        xn = xp
        x_muestra[i+1] = xp
        aceptados += 1
    else:
        x_muestra[i+1] = x_muestra[i]
        no_aceptados += 1
    i += 1

porcentaje_aceptados = 100*aceptados/(aceptados + no_aceptados)
print 'porcentaje aceptados = ' + str(porcentaje_aceptados) + '%'

w = np.zeros(N_muestra)
x = np.linspace(-6, 8, N_muestra)

j = 0
for i in x:
        w[j] = W(i)
        j += 1

w_normalizado = w/13.2616

# graficos

plt.plot(x, w_normalizado, color='r', linewidth=2.5, label='Distribucion W(x)')
plt.xlim(-6, 8)
plt.hist(x_muestra, bins=70, color='b', normed=1, label='Histograma',
         alpha=0.5)
plt.title('distribucion W(x) normalizada y generada con algoritmo de \
           metropolis')
plt.xlabel('x')
plt.ylabel('W(x)')
plt.grid(True)
plt.legend(loc='upper left')

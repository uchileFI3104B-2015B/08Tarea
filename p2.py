from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

def W(x):
    '''
    distribucion sin normalizar
    '''
    w = 3.5 * np.exp(- (x - 3) ** 2 / 3.) + 2 * np.exp(- (x + 1.5) ** 2 / 0.5)
    '''
    ahora normalizamos por un valor calculado con wolfram, no alcance a hacerlo
    '''
    norma = 13.2516
    w= w/norma

    return w
    pass


def condicion_Metro(xn, d):
    '''
    aplica condicion de metropolis fijando el parámetro como un número random
    '''
    xp = xn + d * np.random.uniform(- 1, 1)
    if W(xp) / W(xn) > np.random.uniform(0 , 1):
        xn = xp
    return xn
    pass


def es_optimo(d_in, n):
    '''
    Vemos si el paso es optimo, si la mitad de los "n" valores cumplen la condicion de metropolis, entonces retorna true
    '''
    xn = np.zeros(n)
    xn[0] = np.random.uniform(- 8, 8)
    c = 0
    for i in range(1, n):
        xn[i] = condicion_Metro(xn[i-1], d_in)
        if xn[i] == xn[i-1]:
            c += 1
    return c >= n / 2
    pass




n = 100000
n_p = 10000
x = np.linspace(-8, 8, n)
xn = np.zeros(n)
xn[0] = np.random.uniform(- 8, 8)

#seleccionamos un valor de referencia optimo para el criterio de metropolis, y cortamos la teracion cuando lo hayamos
for i in range(1, 10):
    if es_optimo(i, n_p):
        d = i
        print d
        break
for i in range(1, n):
    xn[i] = condicion_Metro(xn[i-1], d)

fig=plt.figure()
fig.clf()
ax1=fig.add_subplot(111)
n, bins, patches = ax1.hist(xn, 100, normed=True)
ax1.plot(x, W(x))
ax1.set_xlabel("X")
ax1.set_ylabel("W(x)")
plt.draw()
plt.show()

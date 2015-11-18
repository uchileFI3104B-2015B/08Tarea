'''
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1994)


def w(x):
    return 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)

def W(x):
    return w(x) / norma

def metropolis(w, xn, d):
    r = np.random.uniform(-1., 1.)
    xp = xn + d * r
    c = np.random.uniform(0., 1.)
    if (w(xp) / w(xn)) > c:
        return xp
    else:
        return xn

def porcentaje_acepta(w, xn, N, d):
    xn_mas_1 = np.zeros(N)
    xn_mas_1[0] = xn
    acepto = 0.
    rechazo = 0.
    for i in range (len(xn_mas_1) - 1):
        xn_mas_1[i+1] = metropolis(w, xn_mas_1[i], d)
        if xn_mas_1[i+1] == xn_mas_1[i]:
            rechazo += 1.
        else:
            acepto += 1.
    porcentaje = 100.0 * acepto / (acepto + rechazo)
    return porcentaje


#Main
#Set up
N=100
#Probamos delta
n=30

xn_0 = 0

d_posible = np.linspace(1., 10., n)
porcentaje = np.zeros(n)
for i in range(n):
    porcentajes = porcentaje_acepta(w, xn_0, N, d_posible[i])
    porcentaje[i] = np.copy(porcentajes)

for i in range(n):
    if porcentaje[i] >= 49 and porcentaje[i] <= 51:
        d = d_posible[i]
        break
print d



x_int=np.linspace(-10, 10, 1000)
norma = np.trapz(w(x_int), x_int)

fig2 = plt.figure(2)
fig2.clf()
ax2 = fig2.add_subplot(111)
plt.plot(d_posible, porcentaje, '-o', color='r')
ax2.set_xlabel("Valor posible de $\delta$")
ax2.set_ylabel("Porcentaje de veces aceptado")
plt.axhline(y=50, color='g')
plt.axvline(x=3.79, linewidth=1, color='0')
plt.show()
plt.draw()

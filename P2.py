import matplotlib.pyplot as p
import numpy as np

np.random.seed(100)


def w(x):
    '''
    La funcion distribucion a evaluar, la constante de normalizacion fue
    calculada a 'mano'
    '''
    a = 3.5 * np.exp(-(x - 3.0)**2 / 3.0) + 2.0 * np.exp(-(x + 1.5)**2 / 0.5)
    constante = 13.2515587081
    return a / constante


def paso_metropolis(w, xn, d):
    '''
    Un paso del algoritmo de Metropolis
    '''
    r = np.random.uniform(-1.0, 1.0)
    xp = xn + d * r
    s = np.random.uniform(0.0, 1.0)
    if w(xp) / w(xn) > s:
        return xp
    else:
        return xn


def algoritmo_metropolis(w, x0, n, d):

    y = np.zeros(n)
    #Guardamos el primer valor de la serie
    y[0] = x0
    # Contador de aceptados 
    k = 0
    for i in range(n-1):
        y[i+1] = paso_metropolis(w, y[i], d)
        if y[i+1] == y[i]:
            k += 1.
    aceptados = k / n
    return y, aceptados


x = np.linspace(-10., 10., 10**6)
y1 = w(x)
y2, aceptados = algoritmo_metropolis(w, 0.0, 10**7, 4)

print(aceptados)

# Plot
fig = p.figure()
fig.clf()
n, bins, patches = p.hist(y2, normed=1, bins=100)
p.plot(x, y1, 'r')
p.xlabel("$x$")
p.ylabel("$W(x)$")
p.show()

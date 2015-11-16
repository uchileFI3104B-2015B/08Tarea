##############################################################################
'''
Metodos Numericos para la Ciencia e Ingenieria
FI3104-1
Tarea 8
Maximiliano Dirk Vega Aguilera
18.451.231-9
'''
##############################################################################
##############################################################################

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scint

##############################################################################
##############################################################################
# funciones P1

def toro(x,y,z):
    '''
    Toro
    '''
    return z**2 + (np.sqrt(x**2 + y**2) - 3)**2

def cilindro(x,y,z):
    '''
    Cilindro
    '''
    return (x-2)**2 + z**2

def rho(x,y,z):
    '''
    densidad  del cuerpo
    '''
    return 0.5 * (x**2 + y**2 + z**2)

def integrar_montecarlo_cuerpo(rho,N,V):
    '''
    Integra la funcion rho dentro del cuerpo en una caja de volumen 2*10*2=V
    usando el metodo de montecarlo con N muestras.
    Entrega la masa total dentro del cuerpo formado por el toro y el cilindro
    y la posicion del centro de masa en (x, y, z)
    '''
    x = np.random.uniform(1,3,N)   # selecciona punto x dentro de V
    y = np.random.uniform(-4,4,N)  # selecciona punto y dentro de V
    z = np.random.uniform(-1,1,N)  # selecciona punto z dentro de V
    m = 0.
    xm = 0.
    ym = 0.
    zm = 0.
    dentro = 0.
    fuera = 0.
    for i in range(int(N)): # para las N muestras
    # pregunta si el punto esta en la interseccion del toro y el cilindro
        if toro(x[i],y[i],z[i]) <= 1 and cilindro(x[i],y[i],z[i]) <= 1:
            dentro = dentro + 1
            m += rho(x[i],y[i],z[i])
            xm += x[i] * rho(x[i],y[i],z[i])
            ym += y[i] * rho(x[i],y[i],z[i])
            zm += z[i] * rho(x[i],y[i],z[i])
    M = (V * m) / N            # masa total dentro del cuerpo
    CMx = (V * xm) / (M * N)   # posicion x del centro de masa
    CMy = (V * ym) / (M * N)   # posicion y del centro de masa
    CMz = (V * zm) / (M * N)   # posicion z del centro de masa
    fuera = N - dentro
    return M, CMx, CMy, CMz, dentro, fuera

##############################################################################
# funciones P2

def w(x):
    '''
    entrega la distribucion de numeros a obtener (no normalizada)
    '''
    W = 3.5 * np.exp((-(x - 3.)**2) / 3.) + 2. * np.exp((-(x + 1.5)**2) / 0.5)
    return W

def avanza_metropolis(w,xn,d):
    '''
    avanza un paso el algoritmo metropolis
    '''
    r = np.random.uniform(-1., 1.)        # variable aleatoria ~U(-1,1)
    xp = xn + d * r                       # distribucion proposicion
    criterio = np.random.uniform(0., 1.)  # criterio de metropolis
    # se prueba contra criterio de metropolis
    if w(xp) / w(xn) > criterio:
        return xp    # se acepta
    else:
        return xn    # se rechaza

def itera_metropolis(w,xn,d,N):
    '''
    genera una muestra aleatoria mediante el algoritmo de metropolis
    segun la distribucion dada por la funcion w
    '''
    x = np.zeros(N)
    x[0] = np.copy(xn)
    aceptado = 0.
    rechazado = 0.
    for i in range(len(x)-1): # itera el algoritmo metropolis para N valores
        x[i+1] = avanza_metropolis(w, x[i], d)
        if x[i+1] != x[i]:
            aceptado += 1.  # cuenta los xp aceptados
        else:
            rechazado += 1. # cuenta los xp rechazadoss
    return x


##############################################################################
##############################################################################
# P1
'''
toro : z**2 + (sqrt(x**2 + y**2)-3)**2 <= 1
radio mayor 4 y radio menor 2
cilindro : (x-2)**2 + z**2 <= 1
rho(x,y,z) = 0.5*(x**2 + y**2 + z**2)
estimar posicion del centro de masa
rcm= 1/M * int(r*rho(r)dV)
Caja mas pequenha que contiene al cuerpo ([1,3],[-4,4],[-1,1])
'''
#np.random.seed(24)
'''
N = 1e5     # numero de muestras
V = 2.*8.*2.  # volumen de una caja que contiene el cuerpo
R = integrar_montecarlo_cuerpo(rho,N,V)  # se resuelve el problema

print 'Masa total de cuerpo =', R[0]
print 'Posicion del centro de masa = (', R[1],',',R[2],',',R[3],')'
'''
##############################################################################
##############################################################################
# P2
'''
w(x) = 3.5*exp((-(x-3)**2)/3) + 2*exp((-(x+1.5)**2)/0.5)
xp = xn +d*r
r es uniforme(-1,1)
generar muestra de unos 10 millones de puntos
'''
x1 = np.linspace(-10., 10., 10**3)
W1 = w(x1)  # distribucion analitica

# distribucion por metropolis
W2 = itera_metropolis(w, 0., 2., 10**5)

integral = scint.trapz(W1, x=x1) # integral para normalizar

plt.plot(x1, W1/integral, label = 'W(x) analitica')
plt.hist(W2, bins=10**2, normed=1, label = 'W(x) metropolis')

plt.title('Distribucion de muestra aleatoria de W(x)')
plt.xlabel("$x$")
plt.ylabel("$W(x)$")
plt.legend()
plt.show()


##############################################################################
##############################################################################
# puntos extra



##############################################################################
##############################################################################
# cosas



##############################################################################

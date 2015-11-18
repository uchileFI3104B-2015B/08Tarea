
# coding: utf-8

# In[3]:

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# P1 Tarea 8

np.random.seed(55)


class Centro_de_masa(object):
    def __init__(self, vol_caja, num_puntos, a, b, c):
        '''Inicializa la clase Centro de masa con las
        dimensiones del volumen de la caja para el
        metodo de monte carlo y define en variables la
        cantidad de puntos aleatorios a usar dentro de la
        caja'''
        self.V0 = vol_caja  # Arreglo con largos de la caja [lx, ly, lz]
        self.V0num = vol_caja[0] * vol_caja[1] * vol_caja[2]
        self.N = num_puntos
        self.a = a
        self.b = b
        self.c = c

    def interseccion(self, ecs, x, y, z):
        '''Función que intersecta dos ecuaciones dentro
        del arreglo ecs'''
        return (ecs[0](x, y, z) and ecs[1](x, y, z)) == True

    def calcula_CM(self, ecs, densidad):
        '''Recibe como argumentos ecuaciones que describen
        a un solido rigido, su densidad y calcula el centro
        de masa del solido'''
        sumx = 0
        sumy = 0
        sumz = 0
        sumM = 0
        for i in range(self.N):
            x = self.V0[0] * np.random.random_sample() + self.a
            y = self.V0[1] * np.random.random_sample() + self.b
            z = self.V0[2] * np.random.random_sample() + self.c
            if self.interseccion(ecs, x, y, z) is True:
                sumx += x * densidad(x, y, z) * self.V0num / self.N
                sumy += y * densidad(x, y, z) * self.V0num / self.N
                sumz += z * densidad(x, y, z) * self.V0num / self.N
                sumM += densidad(x, y, z) * self.V0num / self.N
        CMX = sumx / sumM
        CMY = sumy / sumM
        CMZ = sumz / sumM
        CM = [CMX, CMY, CMZ]
        return CM

    def itera_CM_N_veces(self, ecs, densidad, num_ejecuciones):
        '''Entrega promedio de CM y su desviacion estandar '''
        n = num_ejecuciones
        CMXarray = np.zeros(num_ejecuciones)
        CMYarray = np.zeros(num_ejecuciones)
        CMZarray = np.zeros(num_ejecuciones)
        for i in range(num_ejecuciones):
            CM = self.calcula_CM(ecs, densidad)
            CMXarray[i] = CM[0]
            CMYarray[i] = CM[1]
            CMZarray[i] = CM[2]
        CMmean = [np.mean(CMXarray), np.mean(CMYarray), np.mean(CMZarray)]
        CMstd = [np.std(CMXarray), np.std(CMYarray), np.std(CMZarray)]
        return CMmean, CMstd


# Main Setup P1


def toro(x, y, z):
    toro = z**2 + (np.sqrt(x**2 + y**2) - 3)**2 <= 1
    return toro


def cilindro(x, y, z):
    cilindro = (x-2)**2 + z**2 <= 1
    return cilindro


def densidad(x, y, z):
    rho = 0.5 * (x**2 + y**2 + z**2)
    return rho


N = 1000
Nejecuciones = 100
V = [8, 8, 2]
'''El toro esta en el plano xy y el
cilindo esta acostado en el plano xy tambien'''
a, b, c = [-4, -4, -1]
solido = Centro_de_masa(V, N, a, b, c)
CM = solido.calcula_CM([toro, cilindro], densidad)
CMmean, CMstd = solido.itera_CM_N_veces([toro, cilindro],
                                        densidad, Nejecuciones)
print "Centro de masa (cx, cy, cz) para una ejecucion = ", CM
print "Centro de masa promedio despues de N ejecuciones = ", CMmean
print "Desviacion estandar para el centro de masa", CMstd

# P2 Tarea 8

# valor int w(x) -inf<=x<=inf = 13.2516


class Metropolis(object):
    def __init__(self, x0, xp, W):  # W es una funcion densidad
        '''Inicializa la clase Metropolis
        que usa el metodo de Metropolis para
        entregar una muestra de N numeros de
        una variable aleatoria con una distribucion W(x),
        dada una distribucion proposicion xp y
        una semilla x0'''
        self.x0 = x0
        self.xp = xp
        self.densidad = W

    def metropolis(self, sample_size, delta):
        '''Recibe como argumentos un tamano para la
        muestra que se quiere y una constante delta
        y entrega una muestra con un numero de datos
        igual a el tamano de la muestra
        por el metodo de metropolis'''
        xn = np.zeros(sample_size)
        r = np.random.uniform(low=-1.0, high=1.0,
                              size=sample_size - 1)
        xn[0] = self.x0
        contador = 0  # Cuenta las prop. aceptadas
        j = 1
        for i in r:
            xp = self.xp(xn[j-1], i, delta)
            if (self.densidad(xp) / self.densidad(xn[j-1]) >
               np.random.uniform(low=0.0, high=1.0, size=None)):
                xn[j] = xp
                contador += 1
            else:
                xn[j] = xn[j-1]
            j += 1
        return xn, contador


def omega(x):  # sin normalizar
    omega = ((3.5 * np.exp((-(x-3)**2) / 3.0) +
              2 * np.exp((-(x + 1.5)**2) / 0.5)))
    return omega


def xp(x0, r, delta):
    xp = x0 + delta * r
    return xp


# Main Setu P2

x0 = 10
xpf = xp
W = omega
delta = 0.5  # con este valor se aceptan al menos el 50% de prop.
size_muestra = 10000000
omegaobj = Metropolis(x0, xpf, W)
muestra = omegaobj.metropolis(size_muestra, delta)[0]
Naceptados = omegaobj.metropolis(size_muestra, delta)[1]
print "Numero de proposicones aceptadas = ", Naceptados
sortedm = np.sort(muestra)
densidad = np.zeros(size_muestra)
x = np.linspace(sortedm[0], sortedm[size_muestra - 1], num=size_muestra)
for i in range(size_muestra):
    densidad[i] = (1 / 13.2516) * omega(x[i])  # densidad normalizada
fig1 = plt.figure(1)
fig1.clf()
plt.plot(x, densidad, 'r-')
plt.hist(muestra, bins=100, range=[-2.7, 6],
         histtype="stepfilled", normed=True)
plt.xlim(-2.7, 6)
plt.xlabel('Valores de la variable aleatoria (unidades)')
plt.ylabel('Frecuencia (unidades)')
plt.title('Histograma para una muestra de una v.a. \n (con tamano = ' +
          str(size_muestra) + ')')
fig1.savefig('metropolis')
plt.grid(True)
plt.show()

'''
# Puntos Extra

x02 = 10
xpf2 = xp
W2 = omega
delta2 = 0.5  # con este valor se aceptan al menos el 50% de prop.
size_muestra2 = 10000
N = 100
muestravarios = np.zeros((N, size_muestra2))
for i in range(N):
    np.random.seed(N+i)
    omegaobj2 = Metropolis(x02, xpf2, W2)
    muestra2 = omegaobj2.metropolis(size_muestra2, delta2)[0]
    sortedm2 = np.sort(muestra2)
    muestravarios[i, :] = sortedm2
omega2 = np.zeros(size_muestra2)
for k in range(size_muestra2):
    omega2[k] = (1 / 13.2516) * omega(muestra2[k])
error = np.zeros(size_muestra2)
for j in range(size_muestra2):
    error[j] = np.std(muestravarios[:, j])
fig2 = plt.figure(2)
fig2.clf()
plt.errorbar(muestra2, omega2, yerr=error)
plt.hist(muestra2, bins=500, histtype="stepfilled", normed=True)
plt.xlim(-2.7, 6)
plt.xlabel('Valores de la variable aleatoria (unidades)')
plt.ylabel('Frecuencia (unidades)')
plt.title('Histograma con barra de errores \n (con tamano = ' +
          str(size_muestra2) + ')')
fig2.savefig('ptosextra')
plt.grid(True)
plt.show()  # No se probo
'''


# In[ ]:




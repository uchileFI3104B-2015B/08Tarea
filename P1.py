import numpy as np
from math import *

def densidad(x, y, z):
    '''Recibe coordenadas espaciales x, y, z
    Retorna valor de la densidad en ese punto
    Si coordenadas caen fuera del objeto retorna 0'''

    # Evalua punto en funcion del Cilindro
    cil_val = (x - 2)**2 + z**2

    if cil_val <= 1:

        # Si el punto esta dentro del Cilindro se revisa el Toro
        tor_val = z**2 + (sqrt(x**2 + y**2) - 3)**2

        if tor_val <= 1:

            # Se retorna densidad dentro del solido
            return 0.5 * (x**2 + y**2 + z**2)

    # Punto esta fuera del solido
    return 0.0

''' Algoritmo de Monte Carlo '''

np.random.seed(123)

N = 1e6  # Cantidad de puntos de muestreo

s_M = s_x = s_y = s_z = 0.0  # Se inicializan las sumas a acumular
var_M = var_x = var_y = var_z = 0.0

vol = 2.0 * sqrt(15.0) * 2.0 * 2.0  # Volumen W, espacio a samplear

i = 0
while i < N:

    # Se genera punto al azar dentro de W
    x = np.random.uniform(1.0, 3.0)
    y = np.random.uniform(-sqrt(15.0), sqrt(15.0))
    z = np.random.uniform(-1.0, 1.0)

    # Se evalua densidad una vez por punto
    dens = densidad(x, y, z)

    s_M += dens
    s_x += x * dens
    s_y += y * dens
    s_z += z * dens

    var_M += dens**2
    var_x += (x * dens)**2
    var_y += (y * dens)**2
    var_z += (z * dens)**2

    i += 1

# Valor de las integrales
M = vol * s_M / N
Tx = vol / N * s_x
Ty = vol / N * s_y
Tz = vol / N * s_z

# Valor del error
dM = vol * sqrt((var_M / N - (s_M / N)**2) / N)
dTx = vol * sqrt((var_x / N - (s_x / N)**2) / N)
dTy = vol * sqrt((var_y / N - (s_y / N)**2) / N)
dTz = vol * sqrt((var_z / N - (s_z / N)**2) / N)

# Calculo de posicion centro de masa (cm) y error
x_cm = Tx / M
y_cm = Ty / M
z_cm = Tz / M

dx_cm = x_cm * sqrt((dTx/Tx)**2 + (dM/M)**2)
dy_cm = y_cm * sqrt((dTy/Ty)**2 + (dM/M)**2)
dz_cm = z_cm * sqrt((dTz/Tz)**2 + (dM/M)**2)


print('masa = ' + str(M) + ' ' + u'\u00B1 ' + str(dM))
print('x_cm = ' + str(x_cm) + ' ' + u'\u00B1 ' + str(dx_cm))
print('y_cm = ' + str(y_cm) + ' ' + u'\u00B1 ' + str(dy_cm))
print('z_cm = ' + str(z_cm) + ' ' + u'\u00B1 ' + str(dz_cm))

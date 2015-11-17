import numpy as np


def den(x, y, z):
    density = 0.5 * (x**2 + y**2 + z**2)
    return density


N = 5000  # número de puntos de la muestra
sum_d = 0
sum_x = 0
sum_y = 0
sum_z = 0
var_d = 0
var_x = 0
var_y = 0
var_z = 0
vol = 2 * 8 * 2  # rectángulo que encierra el volumen considerado

for i in range(N):
    x = 1 + 2 * np.random.uniform(0, 1)  # punto random en el rango de x
    y = -4 + 8 * np.random.uniform(0, 1)  # punto random en el rango de y
    z = -1 + 2 * np.random.uniform(0, 1)  # punto random en el rango de z
    if (z**2 + (np.sqrt(x**2 + y**2) - 3)**2) <= 1:  # si está en el toro
        if ((x-2)**2 + z**2) <= 1:  # si está en el cilindro
            sum_d += den(x, y, z)
            sum_x += x * den(x, y, z)
            sum_y += y * den(x, y, z)
            sum_z += z * den(x, y, z)
            var_d += (den(x, y, z))**2
            var_x += (x * den(x, y, z))**2
            var_y += (y * den(x, y, z))**2
            var_z += (z * den(x, y, z))**2

w = vol * (sum_d / N)
x = vol * (sum_x / N)
y = vol * (sum_y / N)
z = vol * (sum_z / N)
dw = vol * np.sqrt(((var_d / N) - (sum_d / N)**2) / N)  # error en la masa
dx = vol * np.sqrt(((var_x / N) - (sum_x / N)**2) / N)  # error en x
dy = vol * np.sqrt(((var_y / N) - (sum_y / N)**2) / N)  # error en y
dz = vol * np.sqrt(((var_z / N) - (sum_z / N)**2) / N)  # error en z

centro_x = x / w
centro_y = y / w
centro_z = z / w

error_x = (x / w) * np.sqrt((dx / x)**2 + (dw / w)**2)
error_y = (y / w) * np.sqrt((dy / y)**2 + (dw / w)**2)
error_z = (z / w) * np.sqrt((dz / z)**2 + (dw / w)**2)

print(centro_x)
print(centro_y)
print(centro_z)

print(error_x)
print(error_y)
print(error_z)

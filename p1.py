import numpy as np


def densidad(x, y, z):
    density = 0.5 * (x**2 + y**2 + z**2)
    return density


N = 5000  # número de puntos de la muestra
sum_d = sum_x = sum_y = sum_z = var_d = var_x = var_y = var_z = 0
vol = 2 * 8 * 2  # rectángulo que encierra el volumen considerado

for i in range(N): #asignamos al azar los valores de la coordenada X,Y, y Z
    x = 1 + 2 * np.random.uniform(0, 1)
    y = -4 + 8 * np.random.uniform(0, 1)
    z = -1 + 2 * np.random.uniform(0, 1)
    if (z**2 + (np.sqrt(x**2 + y**2) - 3)**2) <= 1:  # nos aseguramos de que esté en el toro
        if ((x-2)**2 + z**2) <= 1:  # lo mismo para el cilindro
             #Ahora "integramos"
            sum_d += densidad(x, y, z)           #Masa
            sum_x += x * densidad(x, y, z)       #rho*x
            sum_y += y * densidad(x, y, z)       #rho*y
            sum_z += z * densidad(x, y, z)       #rho*z
            var_d += (densidad(x, y, z))**2         #varianzas de rho,x,y,z  respectivamente
            var_x += (x * densidad(x, y, z))**2
            var_y += (y * densidad(x, y, z))**2
            var_z += (z * densidad(x, y, z))**2

w = vol * (sum_d / N)
x = vol * (sum_x / N)
y = vol * (sum_y / N)
z = vol * (sum_z / N)
dw = vol * np.sqrt(((var_d / N) - (sum_d / N)**2) / N)  # error en la masa
dx = vol * np.sqrt(((var_x / N) - (sum_x / N)**2) / N)  # error en x
dy = vol * np.sqrt(((var_y / N) - (sum_y / N)**2) / N)  # error en y
dz = vol * np.sqrt(((var_z / N) - (sum_z / N)**2) / N)  # error en z

posicion_x = x / w
posicion_y = y / w
posicion_z = z / w

error_x = (x / w) * np.sqrt((dx / x)**2 + (dw / w)**2)
error_y = (y / w) * np.sqrt((dy / y)**2 + (dw / w)**2)
error_z = (z / w) * np.sqrt((dz / z)**2 + (dw / w)**2)

print(posicion_x)
print(posicion_y)
print(posicion_z)

print(error_x)
print(error_y)
print(error_z)

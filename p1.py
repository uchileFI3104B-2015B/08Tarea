from __future__ import division
import numpy as np

def densidad(x, y, z):
    return 0.5 * (x**2 + y**2 + z**2)


volumen = 8.0 * 12.0 * 2.0

suma_w = 0.0
suma_wx = 0.0
suma_wy = 0.0
suma_wz = 0.0
var_w = 0.0
var_wx = 0.0
var_wy = 0.0
var_wz = 0.0

np.random.seed(212)
n = (int)(1e5)
x = np.random.uniform(-4, 4, n)
y = np.random.uniform(-6, 6, n)
z = np.random.uniform(-1, 1, n)

for i in range(n):
    if z[i]**2 + ( np.sqrt(x[i]**2 + y[i]**2) - 3 )**2 <=1:
        if (x[i]-2)**2 + z[i]**2 <=1:
            suma_w += densidad(x[i], y[i], z[i])
            suma_wx += x[i] * densidad(x[i], y[i], z[i])
            suma_wy += y[i] * densidad(x[i], y[i], z[i])
            suma_wz += z[i] * densidad(x[i], y[i], z[i])

weight = volumen * suma_w / n
x_momento = volumen * suma_wx / n
y_momento = volumen * suma_wy / n
z_momento = volumen * suma_wz / n

print x_momento / weight
print y_momento / weight
print z_momento / weight

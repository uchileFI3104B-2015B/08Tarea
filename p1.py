from __future__ import division
import numpy as np

def densidad(x, y, z):
    return 0.5 * (x**2 + y**2 + z**2)


volumen = 3.0 * 8.0 * 2.0

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
x = np.random.uniform(1, 4, n)
y = np.random.uniform(-4, 4, n)
z = np.random.uniform(-1, 1, n)


for i in range(n):
    if z[i]**2 + ( np.sqrt(x[i]**2 + y[i]**2) - 3 )**2 <=1:
        if (x[i]-2)**2 + z[i]**2 <=1:
            suma_w += densidad(x[i], y[i], z[i])
            suma_wx += x[i] * densidad(x[i], y[i], z[i])
            suma_wy += y[i] * densidad(x[i], y[i], z[i])
            suma_wz += z[i] * densidad(x[i], y[i], z[i])
            var_w += densidad(x[i], y[i], z[i])**2
            var_wx += (x[i] * densidad(x[i], y[i], z[i]))**2
            var_wy += (y[i] * densidad(x[i], y[i], z[i]))**2
            var_wz += (z[i] * densidad(x[i], y[i], z[i]))**2

weight = volumen * suma_w / n
x_momento = volumen * suma_wx / n
y_momento = volumen * suma_wy / n
z_momento = volumen * suma_wz / n

# desviaciones estandar (error)
desv_std_w = volumen * np.sqrt((var_w / n - (suma_w / n)**2) / n)
desv_std_mom_x = volumen * np.sqrt((var_wx / n - (suma_wx / n)**2) / n)
desv_std_mom_y = volumen * np.sqrt((var_wy / n - (suma_wy / n)**2) / n)
desv_std_mom_z = volumen * np.sqrt((var_wz / n - (suma_wz / n)**2) / n)

x_cm = x_momento / weight
y_cm = y_momento / weight
z_cm = z_momento / weight

# errores asociados (desviaciones estandar)
err_x_cm = x_cm * np.sqrt((desv_std_mom_x/x_momento)**2+(desv_std_w/weight)**2)
err_y_cm = y_cm * np.sqrt((desv_std_mom_y/y_momento)**2+(desv_std_w/weight)**2)
err_z_cm = z_cm * np.sqrt((desv_std_mom_z/z_momento)**2+(desv_std_w/weight)**2)

print x_cm, y_cm, z_cm
print err_x_cm, err_y_cm, err_z_cm

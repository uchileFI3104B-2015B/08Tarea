'''
Este script grafica la superficie de un toro con ecuacion
z^2 + (sqrt(x^2+y^2)-3)^2 = 1 y la superficie de un cilindro con
ecuacion (x-2)^2 + z^2 = 1.
'''
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# primer plot, toro
angulo = np.linspace(0, 2 * np.pi, 30)
theta, phi = np.meshgrid(angulo, angulo)
r, R = 1., 3.
X = (R + r * np.cos(phi)) * np.cos(theta)
Y = (R + r * np.cos(phi)) * np.sin(theta)
Z = r * np.sin(phi)

fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, color='w', rstride=1, cstride=1)

# segundo plot, cilindro
x = np.linspace(1, 3, 20)
xc = x - 2
y = np.linspace(-6, 6, 20)
Xc, Yc = np.meshgrid(xc, y)
X = np.meshgrid(x)
Zc = np.sqrt(1.0 - Xc**2.0)

ax.plot_surface(X, Yc, -Zc, color='w', rstride=1, cstride=1)
ax.plot_surface(X, Yc, Zc, color='w', rstride=1, cstride=1)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.view_init(elev=75, azim=60)
plt.show()
plt.draw()
plt.savefig('volumen.png')

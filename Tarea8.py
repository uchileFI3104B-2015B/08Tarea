import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(1, 3, 101)
y = np.linspace(-4, 4, 401)
z = np.linspace(-1, 1, 101)

Puntos = []
Densidades = []


for a in x:
    for b in y:
        for c in z:
            if c**2 + ( (a**2 + b**2)**(0.5) - 3)**2 <=1 and c**2 +(a - 2)**2 <=1:
                Puntos.append([a, b, c])
   
xX= []
yY=[]
zZ=[]
sumaX = 0
sumaY = 0
sumaZ = 0
sumaD = 0

for i in range(len(Puntos)):
	xX.append(Puntos[i][0])
	yY.append(Puntos[i][1])
	zZ.append(Puntos[i][2])

for a in Puntos:
    p = 0.5 * ( (a[0])**2 + (a[1])**2 + (a[2])**2 )
    Densidades.append(p)

for a in range(len(Puntos)):
    sumaX += Puntos[a][0]*Densidades[a]
    sumaY+= Puntos[a][1]*Densidades[a]
    sumaZ += Puntos[a][2]*Densidades[a]
    sumaD += Densidades[a]

Xcm = sumaX / sumaD
Ycm = sumaY / sumaD
Zcm = sumaZ / sumaD

print('El centro de masa esta en ('+str(round(Xcm, 3))+', '+str(round(Ycm, 3))+', '+str(round(Zcm, 3))+').')

'''
fig=plt.figure(1)
fig.clf()
ax=fig.add_subplot(111,projection='3d')
ax.plot_wireframe(xX, yY, zZ)     
plt.title(':^)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.set_zlim(-4,4)
#fig.savefig('Atractor('+str(xp)+', '+str(yp)+', '+str(zp)+').png')
plt.show()
'''

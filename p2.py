from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def W_x (x):

    W_x = 3.5 * np.exp(-(x - 3)**2 / 3) + 2* np.exp( - (x + 15)**2 / 0.5)
    return W_x / 13.2516



def metropolis (xn ,d ):

    xp = xn + d * np.random.uniform(-1.1)
    if W_x(xp) / W_x(xn) > np.random.uniform(0,1):
        xn=xp
    return xn


# set

num_pasos = 10**7
n_p = 10**4
x = np.linspace (-8,8,num_pasos)
xn = np.zeros(num_pasos)
xn[0] = np.random.uniform(-8,8)



for i in range(1, num_pasos):
    xn[i]=  metropolis(xn[i-1],4)


# ploteos

fig =  plt.figure()
fig.clf()
axis1 = fig.add_subplot(1 ,1 ,1)
num_pasos, bins , patches = axis1.hist(xn, 100, normed= True)
axis1.plot(x , W_x(x))
axis1.set_xlabel ("x")
axis1.set_ylabel ("W(x)")
plt.draw()
plt.show()

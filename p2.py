import matplotlib.pyplot as plt
import numpy as np

def w(x):
    funcion = 3.5 * np.exp(-(x - 3.)**2 / 3.) + 2. * np.exp(-2 * (x + 1.5)**2)
    return funcion

x=np.linspace(-10,10,300)
fig = plt.figure(1)
fig.clf()
plt.plot(x,w(x), '-o')
plt.show()
plt.draw()
plt.savefig('w(x).png')

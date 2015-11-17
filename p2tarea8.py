import numpy as np
import matplotlib.pyplot as plt


def W(x):
    w = (3.5 * np.exp(-(x - 2)**2 / 3) +
         2 * np.exp(-(x + 1.5)**2 / 0.5))
    return w

def prop(x):
    r = np.random.uniform(-1, 1)
    xp = x + r * delta
    return xp

delta = raw_input("Ingresar delta:")
semilla = raw_input("Ingresar semilla:")
N = 10000000

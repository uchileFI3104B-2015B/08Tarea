from __future__ import division
import numpy as np

densidad = 1
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

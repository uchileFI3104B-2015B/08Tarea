#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

np.random.seed(347)
DELTA = 2

def W(x):
    return 3.5*np.exp(-((x - 3)**2)/3) + 2*np.exp(-((x + 1.5)**2)/0.5)

def proposicion(xn):
    r = np.random.uniform(low=-1,high=1)
    return xp = xn + r*DELTA

X = []

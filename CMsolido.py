#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def in_toro(x, y, z):
    return z**2 + (np.sqrt(x**2 + y**2) - 3)**2 <= 1

def in_cilindro(x, z):
    return (x - 2)**2 + z**2 <= 1

def densidad(x, y, z):
    return 0.5 * (x**2 + y**2 + z**2)

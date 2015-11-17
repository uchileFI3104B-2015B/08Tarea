# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:23:27 2015

@author: splatt
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math

np.random.seed(7000)
N = 100000
rand = np.random.uniform(low=0.0, high=1.0, size=N*3+3)
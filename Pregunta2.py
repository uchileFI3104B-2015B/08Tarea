# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:38:47 2015

@author: splatt
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def W(x):
    return (3.5*np.exp((-((x-3)**2))/3.)+2.*np.exp((-((x+1.5)**2))/0.5))
from __future__ import division
from math import *
from scipy import integrate as int
from scipy import optimize
from scipy.integrate import ode
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy as n #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp
from mpl_toolkits.mplot3d import Axes3D
import random

N=1000000  #numero de puntos aleatorios a generar

v=n.zeros((3,N))  #matriz de puntos aleatorios

def t(x,y,z):
    '''funcion del toro'''
    return z**2+(n.sqrt(x**2+y**2)-3)**2

def c(x,y,z):
    '''funcion del cono'''
    return (x-2)**2+z**2

def rho(x,y,z):
    '''funcion densidad'''
    return 1/2*(x**2+y**2+z**2)

contador=0   #sumatoria de rho
contadorx=0    #sumatoria de x rho
contadory=0    #sumatoria de y rho
contadorz=0    #sumatoria de z rho

for i in range(N):
    v[0,i]=random.uniform(1,3)    #se generan los puntos aleatorios
    v[1,i]=random.uniform(-n.sqrt(15),n.sqrt(15))
    v[2,i]=random.uniform(-1,1)

    if t(v[0,i],v[1,i],v[2,i])<=1 and c(v[0,i],v[1,i],v[2,i])<=1:
        #puntos dentro del solido aumentan los contadores
        contadorx=contadorx+v[0,i]*rho(v[0,i],v[1,i],v[2,i])
        contadory=contadory+v[1,i]*rho(v[0,i],v[1,i],v[2,i])
        contadorz=contadorz+v[2,i]*rho(v[0,i],v[1,i],v[2,i])
        contador=contador+rho(v[0,i],v[1,i],v[2,i])
    

m=8*n.sqrt(15)*contador/N  #masa

xg=contadorx/contador   #centros de masa
yg=contadory/contador
zg=contadorz/contador

print xg
print yg
print zg
print m


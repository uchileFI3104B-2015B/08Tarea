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

def W(x):
    '''se define la densidad'''
    return 3.5*n.exp(-((x-3.0)**2)/3.0) +2*n.exp(-2.0*(x+1.5)**2)

N=10000000  #numero de datos a generar
delta=3.6   #constante delta
v=n.zeros(N)  #vector que contiene los valores a generar

v0=0.0  #semilla

v[0]=v0

contador=0  #contador de valores aceptados

for i in range(N-1):
    
    vp=v[i]+delta*random.uniform(-1,1)  #se genera el valor vp
    r=random.uniform(0,1)      #se genera el valor aleatorio r

    if W(vp)/W(v[i])>r:   #condicion de aceptacion
        v[i+1]=vp
        contador=contador+1    #contador de aceptacion

    else:
        v[i+1]=v[i]       #no aceptacion


def area(f):
    '''metodo para calcular el area bajo la curva de densidad'''
    N=100000  #numero de intervalos en que se separa el dominio
    
    x=n.linspace(-10,10,N+1)  #dominio

    h=20.0/N  #paso

    da=n.zeros(N)   #vector que contiene el area acumulada de los trapecios
    da[0]=h*(f(x[0])+f(x[1]))/2

    for i in range(N-1):    #metodo de los trapecios
        da[i+1]=da[i]+h*(f(x[i+2])+f(x[i+1]))/2

    A=da[N-1]    #valor de la integral
    return A
    

X=n.linspace(-5,10, 10001)  
A=area(W)

p.hist(v,bins=10000, normed=True)  #histograma
p.plot(X,W(X)/A, label='densidad normalizada', color='r', lw=2.5) #dens norm
p.xlabel('x')
p.ylabel('W(x)')
p.legend(loc='upper right')
p.title('Histograma')
p.show()

print contador/N  #razon de aceptacion

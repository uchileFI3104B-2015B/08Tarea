from __future__ import division
import numpy as np


def en_solido (x, y ,z):
    # funcion que determina si el punto entregado esta
    # en el solido
    # cilindro
    if ((x - 2)**2 + z**2)<=1 :
        # toroide
        if (z**2 + (np.sqrt(x**2+y**2)-3)**2)<=1:
            return True
        else :
            return False
    else:
        return False


def densidad_punto(x,y,z):
    # funcion que determina la densidad en un punto x,y,z
    return 0.5 * (x**2 + y**2 + z**2)


## set
vol = 48
num_pasos = 10**7

# auxiliares para densiadades
aux_den = 0
aux_x = 0
aux_y = 0
aux_z = 0
# auxiliares para varianzas
var_den = 0
var_x = 0
var_y = 0
var_z = 0



for i in range(0,num_pasos):

    x = 3 * np.random.uniform(0,1) + 1
    y = 8 * np.random.uniform(0,1) - 4
    z = 2 * np.random.uniform(0,1) - 1
    if en_solido(x,y,z):
        aux_den = aux_den + densidad_punto(x,y,z)
        aux_x = aux_x + x * densidad_punto(x,y,z)
        aux_y = aux_y + y * densidad_punto(x,y,z)
        aux_z = aux_z + z * densidad_punto(x,y,z)

        var_den = var_den * densidad_punto(x,y,z)**2
        var_x = var_x + (x * densidad_punto(x,y,z))**2
        var_y = var_y + (y * densidad_punto(x,y,z))**2
        var_z = var_z + (z * densidad_punto(x,y,z))**2
#pesos
peso_tot = vol * aux_den / num_pasos
x = vol * aux_x / num_pasos
y = vol * aux_y / num_pasos
z = vol * aux_z / num_pasos

# centros de masas

cm_x = x / peso_tot
cm_y = y / peso_tot
cm_z = z / peso_tot



# imprimir datos

print ("centro de masas" )
print (cm_x, cm_y, cm_z)
#
# print ("errores del centro de masas")
# print (err_x_tot, err_y_tot,err_z_tot)

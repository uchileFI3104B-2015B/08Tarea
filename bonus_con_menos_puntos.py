'''
Este script lee los datos del archivo con_menos_puntos.txt que corresponden
al valor asociado a los bins en cada repeticion del algoritmo de metropolis.
Obtiene el promedio de cada valor y su respectivo error.
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.loadtxt('con_menos_puntos.txt')
bins_escogido = np.linspace(-10, 10, 51)

suma_ns = np.zeros(50)
for i in range(0, 5050, 50):
    suma_ns += n[i:i+50]

ns_promedio = np.copy(suma_ns)/101.

# queremos formar la parte suma sobre i de (x_i - <x>)^2
suma_diferencia_al_cuadrado = np.zeros(50)
for i in range(0, 5050, 50):
    diferencia = (n[i:i+50]-ns_promedio)
    for i in range(50):
        suma_diferencia_al_cuadrado[i] += diferencia[i]*diferencia[i]

# calculando la desviacion estandar

desviacion_estandar = np.zeros(50)
for i in range(50):
    desviacion_estandar[i] = np.sqrt(suma_diferencia_al_cuadrado[i])/7.

fig = plt.figure(1)
fig.clf()
plt.bar(bins_escogido[:50], ns_promedio,
        width=bins_escogido[1] - bins_escogido[0], color='g', alpha=0.5,
        yerr=desviacion_estandar, error_kw=dict(ecolor='red'))
plt.xlabel('x')
plt.show()
plt.draw()
plt.savefig('bonus_con_menos_puntos.png')

import numpy as n
import matplotlib.pyplot as p
import scipy.integrate as s
# Funciones

def W(x):  # Define W como se presenta
    W = 3.5 * n.exp((-(x - 3)**2) / 3) + 2 * n.exp((-(x + 1.5)**2) / 0.5)
    return W


def MetropolisW(Delta, N):  # Aplica metopolis con Delta y la funcion W
    x = [0]  # Valor inicial
    Acep = 0  # Suma de valores aceptados
    for a in range(N - 1):  # Iteraciones
        r = n.random.uniform(-1, 1)  # Obtención de numero aleatorio
        xp = x[a] + Delta * r  # Calcula el xp
        C = n.random.uniform(0, 1)  # Criterio de metropolis
        if C < W(xp) / W(x[a]):  #Compara
            Decide = xp  # Acepta
            Acep += 1
        else:
            Decide = x[a]  # Rechaza
        x.append(Decide)  #Junta los valores
    Aceptacion = 100 * Acep / (N - 1)  # Calcula el porcentaje de aceptacion
    return x, Aceptacion
# Gerena deltas para buscar el mejor
Deltas = n.linspace(0, 10, 101)
PorcentajeAcep = []  # Junta los porcentajes de aceptacion para comparar

for i in range(len(Deltas)):  # Aplica metropolis a cada delta
    PorcentajeAcep.append(MetropolisW(Deltas[i], 10**5)[1])

Aux = 100  # Variable auxiliar inicial para comparar los porcentajes
DeltasMejores = []  # Junta los deltas que dan aceptacion mas proxima a 50

for i in range(len(PorcentajeAcep)):  #Metodo para encontrar delta
    a = PorcentajeAcep[i]
    if abs(a - 50) < Aux:  # Compara el porcentaje con 50
        Aux = abs(a - 50)  # Ahora ese mínimo se utiliza para comparar
        DeltasMejores.append(Deltas[i])  # Se agrega el delta
DeltaEscogido = DeltasMejores[-1]  # El  ultimo delta agregado es el mejor
print ('Mejor Delta escogido: '+str(DeltaEscogido))
# Plot
fig = p.figure()
p.plot(Deltas, PorcentajeAcep, '.')
p.title('$Porcentaje$ $de$ $Aceptacion$ $v/s$ $\delta$')
p.xlabel('$\delta$')
p.ylabel('$Porcentaje$ $de$ $Aceptacion$')
fig.savefig('Porcentaje aceptacion.png')
p.show()
# Arreglo para x y calculo de las dos formas de las funciones W
x = n.linspace(-10, 10, 1000)
Wanalitica = W(x)
Wmetropolis = MetropolisW(DeltaEscogido, 10**7)[0]  # Aplica metropolis
WanaliticaNorm = Wanalitica / s.trapz(Wanalitica, x)  # Normaliza
# Plot
fig = p.figure()
p.plot(x, WanaliticaNorm, label='$W(x)$ $Analitica$')
# Histograma con 100 barras y normalizado a 1
p.hist(Wmetropolis, bins=10**2, normed=1, label='$W(x)$ $Metropolis$')
p.title('$Distribucion$ $W(x)$ $con$ $\delta$ $=$ '+str(DeltaEscogido))
p.xlabel('$x$')
p.ylabel('$W(x)$')
p.legend(loc='upper left')
fig.savefig('Distribución W(x).png')
p.show()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Aquí va el docstring de mi codigo explicando que cosas hace
'''


def densidad(x, y, z):
    ''' Retorna la densidad del sólido en una coordenada dada '''
    rho = 0.5 + (x**2 + y**2 + z**2)
    return rho


def dentro_toro(x, y, z):
    '''Retorna True si las coordenadas están dentro del toro,
    y False si no lo está'''
    return z**2 + (sqrt(x**2 + y**2) - 3)**2 <= 1


def MC1(N):
    ''' Utiliza el algoritmo de Montecarlo 1 para bla'''
    # N = Numero de puntos
    volumen = 3 * 8 * 2. # intervalo x * intervalo y * intervalo z

    suma_peso = 0
    suma_x = 0
    suma_y = 0
    suma_z = 0

    var_peso = 0
    var_x = 0
    var_y = 0
    var_z = 0

    for i in range(N):
        x = np.random.uniform(1, 4)
        y = np.random.uniform(-4, 4)
        z = np.random.uniform(-1, 1)

        if dentro_toro(x, y, z):
            suma_peso += densidad(x, y, z)
            suma_x += x * densidad(x, y, z)
            suma_y += y * densidad(x, y, z)
            suma_z += z * densidad(x, y, z)
            var_peso += densidad(x, y, z)**2
            var_x += (densidad(x, y, z) * x)**2
            var_y += (densidad(x, y, z) * y)**2
            var_z += (densidad(x, y, z) * z)**2

    integral_peso = volumen * suma_peso / N
    integral_x = volumen * suma_x / N
    integral_y = volumen * suma_y / N
    integral_z = volumen * suma_z / N

    # Errores asociados
    err_peso = volumen * np.sqrt((var_peso / (N - suma_peso)**2 / N) / N)
    err_x = volumen * np.sqrt((var_x / N - (suma_x / N)**2) / N)
    err_y = volumen * np.sqrt((var_y / N - (suma_y / N)**2) / N)
    err_z = volumen * np.sqrt((var_z / N - (suma_z / N)**2) / N)

    Integrales = [integral_peso, integral_x, integral_y, integral_z]
    Errores = [err_peso, err_x, err_y, err_z]

    return [Integrales, Errores]

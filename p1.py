import numpy as np

np.random.seed(1911)


def toro(x, y, z):  # Toro
    return z**2 + (np.sqrt(x**2 + y**2) - 3.)**2


def cilindro(x, y, z):  # Cilindro
    return (x - 2.)**2 + z**2


def en_cuerpo(x, y, z):  # Los puntos estan en el cuerpo?
    if toro(x, y, z) <= 1 and cilindro(x, y, z) <= 1:
        return True
    else:
        return False


def densidad(x, y, z):  # Densidad del cuerpo
    return 0.5 * (x**2 + y**2 + z**2)


def varianza(x, y, z):  # Varianza segun coordenada y peso
    varp = densidad(x, y, z) ** 2
    varx = (densidad(x, y, z) * x) ** 2
    vary = (densidad(x, y, z) * y) ** 2
    varz = (densidad(x, y, z) * z) ** 2
    return (varx, vary, varz, varp)

# Setup
sp = 0
sx = 0
sy = 0
sz = 0
varp = 0
varx = 0
vary = 0
varz = 0
volumen = 2. * 8. * 2.
N = 10**7

# Main
for i in range(0, N):  # Monte Carlo
    x = 1. + 3. * np.random.uniform(0., 1.)
    y = 8. * np.random.uniform(0., 1.) - 4.
    z = 2. * np.random.uniform(0., 1.) - 1.
    if en_cuerpo(x, y, z) == True:
        varianza_i = varianza(x, y, z)
        densidad_i = densidad(x, y, z)

        sx += x * densidad_i
        sy += y * densidad_i
        sz += z * densidad_i
        sp += densidad(x, y, z)

        varx += varianza_i[0]
        vary += varianza_i[1]
        varz += varianza_i[2]
        varp += varianza_i[3]

peso = volumen * sp / N
x = volumen * sx / (N * peso)
y = volumen * sy / (N * peso)
z = volumen * sz / (N * peso)

print 'Centro de masa cuerpo = (', x, y, z, ')'

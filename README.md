# Tarea nro. 7
## FI3104B - Métodos Numéricos para la Ciencia y la Ingeniería
#### Prof. Valentino González

## P1

Estime las posición del centro de masa de un sólido descrito por la intersección
de un toro y un cilindro dados por las siguientes ecuaciones:

<img src="eqs/solid.png" height="80px"/>

> Latex: `{\rm Toro:\ \ } z^2 + \left( \sqrt{x^2 + y^2} - 3 \right)^2 \leq 1\\ {\rm Cilindro:\ \ } (x - 2)^2 + z^2 \leq 1`

La densidad del sólido varía según la siguiente fórmula:

<img src="eqs/densidad.png" height="28px"/>

> Latex: `\rho(x, y, z) = 0.5 * (x^2 + y^2 + z^2)`

Para resolver el problema usando alguno de los métodos de integración de Monte
Carlo, debe definirse un volúmen lo más pequeño posible que englobe al sólido
sobre el cual quiere integrar.

> SUGERENCIA : Vea la sección "Simple Monte Carlo Integration" en Numerical Recipes in
> C.

## P2

Se desea obtener una muestra aleatoria de números con la distribución (no
normalizada)

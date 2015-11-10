# Tarea nro. 8
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

> SUGERENCIA : Vea la sección "Simple Monte Carlo Integration" del libro
> "Numerical Recipes in C".

## P2

Se desea obtener una muestra aleatoria de números con la distribución (no
normalizada) dada por la siguiente ecuación:

<img src="eqs/prob.png" height="55px"/>

> Latex: `W(x) = 3.5 \times \exp\left({\frac{-(x-3)^2}{3}}\right) + 2 \times \exp{\left(\frac{-(x+1.5)^2}{0.5}\right)}`

Utilice el algoritmo de Metrópolis con una distribución proposición xp = xn +
&delta; * r, donde r es una variable aleatoria de la distribución uniforme U(-1,
1). La variable &delta; tiene un valor fijo que Ud. debe determinar. Un buen
valor es aquel para el cual se aceptan aproximadamente 50% de las proposiciones.

Genere una muestra de unos 10 millones de puntos. Para comprobar que su
resultado es adecuado grafique W(x) y un histograma de sus variables aleatorias
ambos apropiadamente normalizadas.


> __PUNTOS EXTRA__ (por 2 puntos extra que puede utilizar en cualquier tarea)
>
> Determine la incertidumbre asociada a cada bin del histograma y grafique el
> histograma con las barras de error asociadas.
>
> La estrategia sugerida para esta parte es realizar una simulación estilo Monte
> Carlo: repita muchas veces (N = 100 o más) el procedimiento completo del
> problema, pero cada vez utilice una semilla distinta, o un punto de partida
> distintos o ambos. El resultado es que obtendrá N histogramas que deben ser
> distintos debido a la naturaleza aleatoria del procedimiento. Para un bin
> dado, con N valores distintos, una forma de definir el tamaño de la barra de
> error es hacerla igual a la desviación estándar de de los N valores para ese
> bin.

__Otras Notas.__

- Utilice `git` durante el desarrollo de la tarea para mantener un historial de
  los cambios realizados. La siguiente [*cheat
  sheet*](https://education.github.com/git-cheat-sheet-education.pdf) le puede
  ser útil. Evaluar el uso efectivo de `git`. Recuerde hacer cambios
  significativos pero relativamente pequeños y guardar seguido.  Evite hacer
  `commits` de código que no compila y deje mensajes que permitan entender los
  cambios realizados.

- Evaluaremos su uso correcto de python. Si define una función relativamente
  larga o con muchos parámetros, recuerde escribir el *doctsring* que describa
  los parametros y que es lo que hace la función.  También recuerde usar nombres
  explicativos para las variables y las funciones.  El mejor nombre es aquel que
  permite entender que hace la función sin tener que leer su implementación.

- Los códigos entregados deben pasar las reglas de
  [PEP8](https://www.python.org/dev/peps/pep-0008/). En la línea de comando
  puede intentar `pep8 <script.py>` y asegurarse de que no hay errores ni
  advertencias. Los comandos `pep8 --show-source <script.py>` y `pep8
  --show-pep8 <script.py>` que vimos en clase le pueden ser útiles. Si es de
  aquellos que resuelven su tarea usando el `ipython notebook`, entonces exporte
  la tarea a un archivo normal de `python` y asegúrese de que pasa el test de
  PEP8.

- La tarea se entrega como un *pull request* en github. El *pull request* debe
  incluir todos los códigos usados además de su informe.

- El informe debe ser entregado en formato *pdf*, este debe ser claro sin
  información ni de más ni de menos.

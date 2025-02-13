# Resolución de Tarea 1 - LL y LR (Fecha: 13-02-2025)

$$
\begin{matrix}
\text{Universidad Simón Bolívar} \\
\text{Departamento de Computación y Tecnología de la Información} \\
\text{CI4721 - Lenguajes de Programación II} \\
\text{Enero - Marzo 2025} \\
\text{Estudiante: Junior Miguel Lara Torres (17-10303)} \\
\text{ } \\
\Large \text{Tarea 1 (10 puntos)} \\
\end{matrix}
$$

## Pregunta 1

### Parte (a)
Se define la gramatica libre de contexto $G = (\text{\\{}J, L, X, V\text{\\}}, \text{\\{}null, true, false, \text{\\{}, \text{\\}}, [, ], :, s, n, ,\text{\\}}, P, J)$ con $P$ formado por:

$$
\large \begin{array}{ccl}
J & \rightarrow & \text{\\{L\\}} \\
  &      |      & [X] \\
L & \rightarrow & s : V \\
  &      |      & L, s : V \\
V & \rightarrow & s \\
  &      |      & n \\
  &      |      & true \\
  &      |      & false \\
  &      |      & null \\
  &      |      & J \\
X & \rightarrow & V \\
  &      |      & V, X\\
\end{array}
$$

> [!NOTE]
> El símbolo $"s"$ representa las cadenas de caracteres y el simbolo $"n"$ representa numeros en $\mathbb{R}$.

Aplicando limpieza para este gramática tenemos $\large G' = (\text{\\{}S, J, L, R, V, X, Y\text{\\}}, \text{\\{} s, n, true, false, null, \text{\\{}, \text{\\}}, [, ], :, ,\text{\\}}, P', S)$ con $P'$ formado por:

$$
\large \begin{array}{ccl}
S & \rightarrow & J \\
J & \rightarrow & \text{\\{L\\}} \\
  &      |      & [X] \\
L & \rightarrow & s : V R\\
R & \rightarrow & , s : V R \\
  &      |      & \lambda \\
V & \rightarrow & s \\
  &      |      & n \\
  &      |      & true \\
  &      |      & false \\
  &      |      & null \\
  &      |      & J \\
X & \rightarrow & V Y \\
Y & \rightarrow & , V Y \\
  &      |      & \lambda \\
\end{array}
$$

### Parte (b)
Se usa la herramienta Parsec en Python. Acá su repositorio de [GitHub](https://github.com/sighingnow/parsec.py) y su liberia oficial en [PyPi Org](https://pypi.org/project/parsec/).

#### Guia de instalación y ejecución

1. Actualiza el sistema, instala Python 3 y sus herramientas de desarrollo.
	```
	sudo apt install python3.12 python3.12-venv python3-pip -y
	```
	* Version de Python usada `Python 3.12.3`.
	* Version de Pip usada `pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)`

2. Clona el repositorio donde estan los archivos de la tarea.
	```
	git clone https://github.com/JMLTUnderCode/Programming_Language_Series.git
	```

3. Dirigirte al directorio de la tarea.
	```
	cd ~/Programming_Language_Series/Lenguajes_II/Tarea_1
	```

4. Crea un Environment
	```
	python3 -m venv env
	```

5. Activa el Environment
	```
	source env/bin/activate
	```
	* El Environment se activa y se muestra el nombre del Environment en la terminal.
	* Para desactivar el Environment, se usa `deactivate`.

6. Instala el Parsec de Python.
	```
	pip install parsec
	```
	* La version de Parsec instalada es `3.17`.
	* A fecha 2/11/2025 Parsec tiene soporte hasta `Python 3.12`. Ver mas informacion de [Parsec](https://pypi.org/project/parsec/#history).
7. Ejecutar el archivo `pregunta_1b.py` con el comando.
	```
	python3 pregunta_1b.py <dir. archivo de prueba>
	```
	Ej.
	```
	python3 pregunta_1b.py tests/0.txt
	```

## Pregunta 2

### Parte (a)

Dada la gramatica $\large IFT = (\text{\\{} E \text{\\}}, \text{\\{} n, +, if, then, else \text{\\}}, P, E)$ con $P$ formado por:

$$
\begin{array}{ccl}
E & \rightarrow & if \text{ E } then \text{ E } else \text{ E } \\
  &  |  & if \text{ E } then \text{ E } \\
  &  |  & \text{E+E} \\
  &  |  & n
\end{array}
$$

La expansión de esta gramatica con un nuevo símbolo inicial no recursivo $S$ queda que $\large IFT' = (\text{\\{}S, E\text{\\}}, \text{\\{} n, +, if, then, else, \text{\\$} \text{\\}}, P', S)$ con $P'$ formado por:

$$
\begin{array}{ccl}
S & \rightarrow & E\$ \\
E & \rightarrow & if \text{ E } then \text{ E } else \text{ E } \\
  &  |  & if \text{ E } then \text{ E } \\
  &  |  & \text{E+E} \\
  &  |  & n
\end{array}
$$

Para el Máquina Característica LR(1) se tiene link directo a [LucidChar](https://lucid.app/lucidchart/761b6e5e-548c-4c82-9262-6d2a5358c6e4/edit?viewport_loc=-11037%2C-7320%2C10330%2C5094%2C0_0&invitationId=inv_57d0e47c-0812-4491-8ad1-a58fdc3d88d2) o a continuacion la imagen representativa.

![Diagrama en blanco - Página 1 (1)](https://github.com/user-attachments/assets/45314af4-9346-4c21-9be4-84e8abf337ff)

### Parte (b)
Enumerando las reglas tal que
* `Regla 1`: + asocia a izquierda. `E + E + E = (E + E) + E`
* `Regla 2`: else se asocia al if más interno. `if E then if E then E else E = if E then (if E then E else E)`
* `Regla 3`: if tiene mayor precedencia que +. `E + if E then E else E + E = E + (if E then E else E) + E`

Ahora se mostraran los estados con conflictos y las acciones a tomar con su respectiva justificación.

* Estado 9:
	```
	E -> E+E. {$, +}
	E -> E.+E {$, +}
 	```
 	* Se aplica REDUCE con `E -> E+E` para satisfacer `Regla 1`.
* Estado 13:
	```
	E -> if E then E. else E {$, +}
	E -> if E then E.        {$, +}
	E -> E.+E                {else, $, +}
	```
   	* Se aplica REDUCE con `E -> if E then E` entre ITEM 2 y 3 para satisfacer `Regla 3`.
* Estado 16:
  	```
	E -> E+E. {then, +}
	E -> E.+E {then, +}
   	```
	* Se aplica REDUCE con `E -> E+E` para satisfacer `Regla 1`.
* Estado 21:
  	```
	E -> if E then E. else E {then, +}
	E -> if E then E.        {then, +}
	E -> E.+E                {else, then, +}
   	```
	* Se aplica REDUCE con `E -> if E then E` entre ITEM 2 y 3 para satisfacer `Regla 3`.
* Estado 24:
  	```
	E -> if E then E else E. {$, +}
	E -> E.+E                {$, +}
   	```
	* Se aplica REDUCE con `E -> if E then E else E` para satisfacer `Regla 3`.
* Estado 25:
  	```
	E -> E+E. {else, $, +}
	E -> E.+E {else, $, +}
   	```
	* Se aplica REDUCE con `E -> E+E` para satisfacer `Regla 1`.
* Estado 30:
  	```
	E -> if E then E. else E {else, $, +}
	E -> if E then E.        {else, $, +}
	E -> E.+E                {else, $, +}
   	```
	* Se aplica SHIFT con `E -> if E then E. else E` entre ITEM 1 y 2 para satisfacer `Regla 2`.
	* Se aplica REDUCE con `E -> if E then E` entre ITEM 2 y 3 para satisfacer `Regla 3`.
* Estado 31:
	```
	E -> if E then E else E. {then, +}
	E -> E.+E                {then, +}
 	```
	* Se aplica REDUCE con `E -> if E then E else E` para satisfacer `Regla 3`.
* Estado 32:
  	```
	E -> E+E. {else, then, +}
	E -> E.+E {else, then, +}
   	```
	* Se aplica REDUCE con `E -> E+E` para satisfacer `Regla 1`.
* Estado 35
	```
	E -> if E then E. else E {else, then, +}
	E -> if E then E.        {else, then, +}
	E -> E.+E                {else, then, +}
 	```
	* Se aplica SHIFT con `E -> if E then E. else E` entre ITEM 1 y 2 para satisfacer `Regla 2`.
 	* Se aplica REDUCE con `E -> if E then E` entre ITEM 2 y 3 para satisfacer `Regla 3`.
* Estado 36:
  	```
	E -> if E then E else E. {else, $, +}
	E -> E.+E                {else, $, +}
   	```
	* Se aplica REDUCE con `E -> if E then E else E` para satisfacer `Regla 3`.
* Estado 38:
  	```
	E -> if E then E else E. {else, then, +}
	E -> E.+E                {else, then, +}
   	```
	* Se aplica REDUCE con `E -> if E then E else E` para satisfacer `Regla 3`.

### Parte (c)

Para el Máquina Característica LALR(1) se tiene link directo a [LucidChar](https://lucid.app/lucidchart/761b6e5e-548c-4c82-9262-6d2a5358c6e4/edit?viewport_loc=-11037%2C-7320%2C10330%2C5094%2C0_0&invitationId=inv_57d0e47c-0812-4491-8ad1-a58fdc3d88d2) o a continuacion la imagen representativa.

![Diagramas Generales - Junior Lara - Página 1](https://github.com/user-attachments/assets/e7f4ef8e-8ae5-453e-a53a-f00d0574982e)

Por otro lado, se mostraran los estados con conflictos y las acciones a tomar con su respectiva justificación.

* Estado 13, 21, 30, 35:
	```
	E → if E then E. else E {else, then, $, +}
	E → if E then E.        {else, then, $, +}
	E → E.+E                {else, then, $, +}
 	```
	* Se aplica SHIFT con `E → if E then E. else E` entre ITEM 1 y 2 para satisfacer `Regla 2`.
 	* Se aplica REDUCE con `E → if E then E.` entre ITEM 2 y 3 para satisfacer `Regla 3`.
* Estado 24, 31, 36, 38:
	```
	E → if E then E else E.	{else, then, $, +}
	E → E.+E                {else, then, $, +}
 	```
	Se aplica REDUCE con `E → if E then E else E.` para satisfacer `Regla 3`.
* Estado 9, 16, 25, 32:
	```
	E → E+E. {else, then, $, +}
	E → E.+E {else, then, $, +}
	```
 	Se aplica REDUCE con `E → E+E.` para satisfacer `Regla 1`.
### Parte (d)

A continuacion de muestra la tabla de acciones basado en la máquina característica LALR(1).
$$
\begin{array}{c|cccccc|c}
\text{States} & \text{if} & \text{then} & \text{else} & \text{+} & \text{n} & \text{\\$} & \text{E} \\
0  & & & & & & &  \\
1  & & & & & & &  \\
2  & & & & & & &  \\
3  & & & & & & &  \\
4  & & & & & & &  \\
5  & & & & & & &  \\
6  & & & & & & &  \\
7  & & & & & & &  \\
\end{array}
$$

Para el procesamiento de la expresion $\large \text{if n + n then if n then n else n + n}$ tenemos que
$$
\begin{array}{c|c|c}
\text{Stack} & \text{Expression} & \text{Action} \\
 & &  \\
 & &  \\
 & &  \\
 & &  \\
 & &  \\
 & &  \\
 & &  \\
 & &  \\
 & &  \\
 & &  \\
\end{array}
$$

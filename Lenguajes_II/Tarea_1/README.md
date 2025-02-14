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

# Indice
- [Resolución de Tarea 1 - LL y LR (Fecha: 13-02-2025)](#resolución-de-tarea-1---ll-y-lr-fecha-13-02-2025)
- [Indice](#indice)
	- [Pregunta 1](#pregunta-1)
		- [Parte (1.a)](#parte-1a)
		- [Parte (1.b)](#parte-1b)
			- [Guia de instalación y ejecución](#guia-de-instalación-y-ejecución)
	- [Pregunta 2](#pregunta-2)
		- [Parte (2.a)](#parte-2a)
		- [Parte (2.b)](#parte-2b)
		- [Parte (2.c)](#parte-2c)
		- [Parte (2.d)](#parte-2d)

## Pregunta 1

### Parte (1.a)
Se define la gramatica libre de contexto $\large G = (\text{\\{}J, L, X, V\text{\\}}, \text{\\{}null, true, false, \text{\\{}, \text{\\}}, [, ], :, s, n, ,\text{\\}}, P, J)$ con $P$ formado por:

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

### Parte (1.b)
Se usa la herramienta Parsec en Python. Acá su repositorio de [GitHub](https://github.com/sighingnow/parsec.py) y su liberia oficial en [PyPi Org](https://pypi.org/project/parsec/).

#### Guia de instalación y ejecución

Especificaciones del sistema donde este programa fue implementado y probado.
```
Distributor ID: Ubuntu
Description:    Ubuntu 24.04.1 LTS
Release:        24.04
Codename:       noble
```

1. Actualizar el sistema, instalar Python 3 y sus herramientas de desarrollo.
	```
	sudo apt install python3.12 python3.12-venv python3-pip -y
	```
	* Version de Python usada `Python 3.12.3`.
	* Version de Pip usada `pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)`

2. Clonar el repositorio donde estan los archivos de la tarea.
	```
	git clone https://github.com/JMLTUnderCode/Programming_Language_Series.git
	```

3. Dirigirse al directorio de la tarea.
	```
	cd ~/Programming_Language_Series/Lenguajes_II/Tarea_1
	```

4. Crear un Environment
	```
	python3 -m venv env
	```

5. Activar el Environment
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

### Parte (2.a)

Dada la gramática $\large IFT = (\text{\\{} E \text{\\}}, \text{\\{} n, +, if, then, else \text{\\}}, P, E)$ con $P$ formado por:

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

Para la Máquina Característica LR(1) se tiene link directo a [LucidChar](https://lucid.app/lucidchart/761b6e5e-548c-4c82-9262-6d2a5358c6e4/edit?viewport_loc=-11037%2C-7320%2C10330%2C5094%2C0_0&invitationId=inv_57d0e47c-0812-4491-8ad1-a58fdc3d88d2) o a continuacion la imagen representativa.

![Diagrama en blanco - Página 1 (1)](https://github.com/user-attachments/assets/45314af4-9346-4c21-9be4-84e8abf337ff)

### Parte (2.b)

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
 	* Se aplica REDUCE con `E -> E+E.` para satisfacer `Regla 1`.
* Estado 13:
	```
	E -> if E then E. else E {$, +}
	E -> if E then E.        {$, +}
	E -> E.+E                {else, $, +}
	```
   	* Se aplica REDUCE con `E -> if E then E.` entre ITEM 2 y 3 para satisfacer `Regla 3`.
* Estado 16:
  	```
	E -> E+E. {then, +}
	E -> E.+E {then, +}
   	```
	* Se aplica REDUCE con `E -> E+E.` para satisfacer `Regla 1`.
* Estado 21:
  	```
	E -> if E then E. else E {then, +}
	E -> if E then E.        {then, +}
	E -> E.+E                {else, then, +}
   	```
	* Se aplica REDUCE con `E -> if E then E.` entre ITEM 2 y 3 para satisfacer `Regla 3`.
* Estado 24:
  	```
	E -> if E then E else E. {$, +}
	E -> E.+E                {$, +}
   	```
	* Se aplica REDUCE con `E -> if E then E else E.` para satisfacer `Regla 3`.
* Estado 25:
  	```
	E -> E+E. {else, $, +}
	E -> E.+E {else, $, +}
   	```
	* Se aplica REDUCE con `E -> E+E.` para satisfacer `Regla 1`.
* Estado 30:
  	```
	E -> if E then E. else E {else, $, +}
	E -> if E then E.        {else, $, +}
	E -> E.+E                {else, $, +}
   	```
	* Se aplica SHIFT con `E -> if E then E. else E` entre ITEM 1 y 2 para satisfacer `Regla 2`.
	* Se aplica REDUCE con `E -> if E then E.` entre ITEM 2 y 3 para satisfacer `Regla 3`.
* Estado 31:
	```
	E -> if E then E else E. {then, +}
	E -> E.+E                {then, +}
 	```
	* Se aplica REDUCE con `E -> if E then E else E.` para satisfacer `Regla 3`.
* Estado 32:
  	```
	E -> E+E. {else, then, +}
	E -> E.+E {else, then, +}
   	```
	* Se aplica REDUCE con `E -> E+E.` para satisfacer `Regla 1`.
* Estado 35
	```
	E -> if E then E. else E {else, then, +}
	E -> if E then E.        {else, then, +}
	E -> E.+E                {else, then, +}
 	```
	* Se aplica SHIFT con `E -> if E then E. else E` entre ITEM 1 y 2 para satisfacer `Regla 2`.
 	* Se aplica REDUCE con `E -> if E then E.` entre ITEM 2 y 3 para satisfacer `Regla 3`.
* Estado 36:
  	```
	E -> if E then E else E. {else, $, +}
	E -> E.+E                {else, $, +}
   	```
	* Se aplica REDUCE con `E -> if E then E else E.` para satisfacer `Regla 3`.
* Estado 38:
  	```
	E -> if E then E else E. {else, then, +}
	E -> E.+E                {else, then, +}
   	```
	* Se aplica REDUCE con `E -> if E then E else E.` para satisfacer `Regla 3`.

### Parte (2.c)

Para la Máquina Característica LALR(1) se tiene link directo a [LucidChar](https://lucid.app/lucidchart/761b6e5e-548c-4c82-9262-6d2a5358c6e4/edit?viewport_loc=-11037%2C-7320%2C10330%2C5094%2C0_0&invitationId=inv_57d0e47c-0812-4491-8ad1-a58fdc3d88d2) o a continuacion la imagen representativa.

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

### Parte (2.d)

Teniendo en cuenta la siguiente enumeracion para las producciones

$$
\begin{array}{cccl}
(P1) & S & \rightarrow & E\$ \\
(P2) & E & \rightarrow & if \text{ E } then \text{ E } else \text{ E } \\
(P3) &  &  |  & if \text{ E } then \text{ E } \\
(P4) &  &  |  & \text{E+E} \\
(P5) &  &  |  & n
\end{array}
$$

A continuacion de muestra la tabla de acciones basado en la máquina característica LALR(1).

| RenameState | States      | if                | then              | else              | +                 | n                 | $                 | E           |
|:-----------:|:-----------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------:|
| 0           | 0           | SHIFT 2,7,14,22   |                   |                   |                   | SHIFT 3,8,15,23   |                   | 1           |
| 1           | 1           |                   |                   |                   | SHIFT 5,11,19,28  |                   | 4                 |             |
| 2           | 4           |                   |                   |                   |                   |                   | REDUCE P1-ACCEPT  |             |
| 3           | 2,7,14,22   | SHIFT 2,7,14,22   |                   |                   |                   | SHIFT 3,8,15,23   |                   | 6,12,20,29  |
| 4           | 6,12,20,29  |                   | SHIFT 10,17,26,33 |                   | SHIFT 5,11,19,28  |                   |                   |             |
| 5           | 10,17,26,33 | SHIFT 2,7,14,22   |                   |                   |                   | SHIFT 3,8,15,23   |                   | 13,21,30,35 |
| 6           | 13,21,30,35 |                   | REDUCE-P3         | SHIFT 18,27,34,37 | REDUCE-P3         |                   | REDUCE-P3         |             |
| 7           | 3,8,15,23   |                   | REDUCE-P5         | REDUCE-P5         | REDUCE-P5         |                   | REDUCE-P5         |             |
| 8           | 5,11,19,28  | SHIFT 2,7,14,22   |                   |                   |                   | SHIFT 3,8,15,23   |                   | 9,16,25,32  |
| 9           | 18,27,34,37 | SHIFT 2,7,14,22   |                   |                   |                   | SHIFT 3,8,15,23   |                   | 24,21,35,38 |
| 10          | 9,16,25,32  |                   | REDUCE-P4         | REDUCE-P4         | REDUCE-P4         |                   | REDUCE-P4         |             |
| 11          | 24,21,35,38 |                   | REDUCE-P2         | REDUCE-P2         | REDUCE-P2         |                   | REDUCE-P2         |             |

Para el procesamiento de la expresion $\large \text{"if n + n then if n then n else n + n"}$ tomemos en consideracion la columna RenameState para facilitar la pila.

| Expression                            | Stack                                 | Action    |
|--------------------------------------:|--------------------------------------:|:---------:|
| if n + n then if n then n else n + n$ | $E_0\$$                               | SHIFT-3   |
|    n + n then if n then n else n + n$ | $E_3E_0\$$                            | SHIFT-7   |
|      + n then if n then n else n + n$ | $E_7E_3E_0\$$                         | REDUCE-P5 |
|      + n then if n then n else n + n$ | $E_4E_3E_0\$$                         | SHIFT-8   |
|        n then if n then n else n + n$ | $E_8E_4E_3E_0\$$                      | SHIFT-7   |
|          then if n then n else n + n$ | $E_7E_8E_4E_3E_0\$$                   | REDUCE-P5 |
|          then if n then n else n + n$ | $E_{10}E_8E_4E_3E_0\$$                | REDUCE-P4 |
|          then if n then n else n + n$ | $E_4E_3E_0\$$                         | SHIFT-5   |
|               if n then n else n + n$ | $E_5E_4E_3E_0\$$                      | SHIFT-3   |
|                  n then n else n + n$ | $E_3E_5E_4E_3E_0\$$                   | SHIFT-7   |
|                    then n else n + n$ | $E_7E_3E_5E_4E_3E_0\$$                | REDUCE-P5 |
|                    then n else n + n$ | $E_4E_3E_5E_4E_3E_0\$$                | SHIFT-5   | 
|                         n else n + n$ | $E_5E_4E_3E_5E_4E_3E_0\$$             | SHIFT-7   |
|                           else n + n$ | $E_7E_5E_4E_3E_5E_4E_3E_0\$$          | REDUCE-P5 |
|                           else n + n$ | $E_6E_5E_4E_3E_5E_4E_3E_0\$$          | SHIFT-9   |
|                                n + n$ | $E_9E_6E_5E_4E_3E_5E_4E_3E_0\$$       | SHIFT-7   |
|                                  + n$ | $E_7E_9E_6E_5E_4E_3E_5E_4E_3E_0\$$    | REDUCE-P5 |
|                                  + n$ | $E_{11}E_9E_6E_5E_4E_3E_5E_4E_3E_0\$$ | REDUCE-P2 |
|                                  + n$ | $E_6E_5E_4E_3E_0\$$                   | REDUCE-P3 |
|                                  + n$ | $E_1E_0\$$                            | SHIFT-8   |
|                                    n$ | $E_8E_1E_0\$$                         | SHIFT-7   |
|                                     $ | $E_7E_8E_1E_0\$$                      | REDUCE-P5 |
|                                     $ | $E_{10}E_8E_1E_0\$$                   | REDUCE-P4 |
|                                     $ | $E_1E_0\$$                            | SHIFT-2   |
|                                       | $E_2E_1E_0\$$                         | REDUCE-P1 |
|                                       |                                       | ACCEPT    |

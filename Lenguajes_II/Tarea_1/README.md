# Resolución de Tarea 1 - LL y LR (Fecha: 13-02-2025)

$\begin{matrix}
\text{Universidad Simón Bolívar} \\
\text{Departamento de Computación y Tecnología de la Información} \\
\text{CI4721 - Lenguajes de Programación II} \\
\text{Enero - Marzo 2025} \\
\text{Estudiante: Junior Miguel Lara Torres (17-10303)} \\
\text{ } \\
\Large \text{Tarea 1 (10 puntos)} \\
\end{matrix}$

## Pregunta 1

### Parte (a)
Se define la gramatica libre de contexto $\large G = (\{J, L, X, V\}, \{null, true, false, \{, \}, [, ], :, s, n, ,\}, P, J)$ con $P$ formado por:

$
\large \begin{matrix}
J & \rightarrow & \{L\} \\
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
\end{matrix}
$

> [!NOTE]
> El valor "s" representa las cadenas de caracteres y el valor "n" representa numeros en $\mathbb{R}$.

Aplicando limpieza para este gramática tenemos $\large G' = (\{S, J, L, R, V, X, Y\}, \{null, true, false, \{, \}, [, ], :, s, n, ,\}, P', S)$ con $P'$ formado por:

$
\large \begin{matrix}
S & \rightarrow & J \\
J & \rightarrow & \{L\} \\
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
\end{matrix}
$

### Parte (b)
Se usa la herramienta [Parsec](https://github.com/sighingnow/parsec.py) de Python.

Guia de instalaciÓn y ejecuciÓn

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

### Parte (b)

### Parte (c)

### Parte (d)
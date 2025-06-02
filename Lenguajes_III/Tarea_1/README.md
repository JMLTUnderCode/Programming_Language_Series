# Resolución de Tarea 1 - Generación de Código (Fecha: 01-06-2025)

$$
\begin{matrix}
\text{Universidad Simón Bolívar} \\
\text{Departamento de Computación y Tecnología de la Información} \\
\text{CI4721 - Lenguajes de Programación II} \\
\text{Abril - Julio 2025} \\
\text{Estudiante: Junior Miguel Lara Torres (17-10303)} \\
\text{ } \\
\Large \text{Tarea 1 (10 puntos)} \\
\end{matrix}
$$

# Indice
- [Resolución de Tarea 1 - Generación de Código (Fecha: 01-06-2025)](#resolución-de-tarea-1---generación-de-código-fecha-01-06-2025)
- [Indice](#indice)
	- [Pregunta 1](#pregunta-1)
	- [Pregunta 2](#pregunta-2)
		- [Parte (2.a)](#parte-2a)
		- [Parte (2.b)](#parte-2b)
		- [Parte (2.c)](#parte-2c)
		- [Parte (2.d)](#parte-2d)
	- [Pregunta 3](#pregunta-3)
		- [Parte (3.a)](#parte-3a)
		- [Parte (3.b)](#parte-3b)
	- [Pregunta 4](#pregunta-4)
		- [Parte (4.a)](#parte-4a)
		- [Parte (4.b)](#parte-4b)
		- [Parte (4.c)](#parte-4c)
		- [Parte (4.d)](#parte-4d)

## Pregunta 1

Se tiene en parte inicial el siguiente conjunto de variables vivas inicial, instrucciones escrito en TAC y se quiere calcular el conjunto de variables vivas y la información de uso futuro antes y después de cada una de éstas.

| Instrucción | Variables Vivas | Uso Futuro |
|:-----------:|:---------------:|:----------:|
| a := b + c  |                 |            |
| b := a / 2  |                 |            |
| b := d - c  |                 |            |
| a := a + d  |                 |            |
| c := b * a  | $\{b, d\}$      | $\text{nextuse(a) = undef} \\ \text{nextuse(b) = undef} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = undef}$ |

* Analizando la Instrucción `c := b * a` tenemos que estan vivas `b` y `a` con uso futuro en el bloque 5.

| Instrucción | Variables Vivas | Uso Futuro |
|:-----------:|:---------------:|:----------:|
| a := b + c  |                 |            |
| b := a / 2  |                 |            |
| b := d - c  |                 |            |
| a := a + d  | $\{a, b, d\}$   | $\text{nextuse(a) = 5} \\ \text{nextuse(b) = 5} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = undef}$ |
| c := b * a  | $\{b, d\}$      | $\text{nextuse(a) = undef} \\ \text{nextuse(b) = undef} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = undef}$ |

* Analizando la Instrucción `a := a + d` tenemos que se conservan las variables vivas (`a`, `b`, `c`) pero hay un cambio en el uso furuto de `a` y `d` en el bloque 4.

| Instrucción | Variables Vivas | Uso Futuro |
|:-----------:|:---------------:|:----------:|
| a := b + c  |                 |            |
| b := a / 2  |                 |            |
| b := d - c  | $\{a, b, d\}$   | $\text{nextuse(a) = 4} \\ \text{nextuse(b) = 5} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = 4}$ |
| a := a + d  | $\{a, b, d\}$   | $\text{nextuse(a) = 5} \\ \text{nextuse(b) = 5} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = undef}$ |
| c := b * a  | $\{b, d\}$      | $\text{nextuse(a) = undef} \\ \text{nextuse(b) = undef} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = undef}$ |

* Analizando la Instrucción `b := a / 2` tenemos que estan vivas `a`, `c` y `d` con uso futuro de 4 para `a` y 3 para `c` y `d`.

| Instrucción | Variables Vivas | Uso Futuro |
|:-----------:|:---------------:|:----------:|
| a := b + c  |                 |            |
| b := a / 2  | $\{a, c, d\}$   | $\text{nextuse(a) = 4} \\ \text{nextuse(b) = undef} \\ \text{nextuse(c) = 3} \\ \text{nextuse(d) = 3}$ |
| b := d - c  | $\{a, b, d\}$   | $\text{nextuse(a) = 4} \\ \text{nextuse(b) = 5} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = 4}$ |
| a := a + d  | $\{a, b, d\}$   | $\text{nextuse(a) = 5} \\ \text{nextuse(b) = 5} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = undef}$ |
| c := b * a  | $\{b, d\}$      | $\text{nextuse(a) = undef} \\ \text{nextuse(b) = undef} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = undef}$ |

* Analizando la Instrucción `a := b + c` tenemos que se conservan las variables vivas (`a`, `b`, `c`) pero hay un cambio en el uso futuro de 2 para `a` y 3 para `c` y `d`.

| Instrucción | Variables Vivas | Uso Futuro |
|:-----------:|:---------------:|:----------:|
| a := b + c  | $\{a, c, d\}$   | $\text{nextuse(a) = 2} \\ \text{nextuse(b) = undef} \\ \text{nextuse(c) = 3} \\ \text{nextuse(d) = 3}$ |
| b := a / 2  | $\{a, c, d\}$   | $\text{nextuse(a) = 4} \\ \text{nextuse(b) = undef} \\ \text{nextuse(c) = 3} \\ \text{nextuse(d) = 3}$ |
| b := d - c  | $\{a, b, d\}$   | $\text{nextuse(a) = 4} \\ \text{nextuse(b) = 5} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = 4}$ |
| a := a + d  | $\{a, b, d\}$   | $\text{nextuse(a) = 5} \\ \text{nextuse(b) = 5} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = undef}$ |
| c := b * a  | $\{b, d\}$      | $\text{nextuse(a) = undef} \\ \text{nextuse(b) = undef} \\ \text{nextuse(c) = undef} \\ \text{nextuse(d) = undef}$ |


## Pregunta 2

### Parte (2.a)

### Parte (2.b)

### Parte (2.c)

### Parte (2.d)


## Pregunta 3

Se responden los siguientes apartado teniendo en cuenta la siguiente instrucción

$$\text{we[have] = to[go[deep]] + er}$$

### Parte (3.a)

El código TAC respectivo es

$$\begin{array}{l} 
\text{t1 := deep * 4} \\ 
\text{t2 := go[t1]}   \\ 
\text{t3 := t2 + er}  \\ 
\text{t4 := t3 * 4}   \\ 
\text{t5 := to[t4]}   \\ 
\text{t6 := have * 4} \\ 
\text{we[t6] := t5} 
\end{array}$$

>[!NOTE]
> En un contexto de arreglos de enteros se multiplica por `4` los índices los enteros se representan en 4 bytes.

### Parte (3.b)

Realizacion las iteraciones respectivas e ilustrando a nivel de las siguientes tablas obtenemos que

- [x] Inicial

| R1 | R2 | R3 |$\|$| we | have | to | go | deep | er | t1 | t2 | t3 | t4 | t5 | t6 |
|----|----|----|----|----|------|----|----|------|----|----|----|----|----|----|----|
|    |    |    |$\|$| we | have | to | go | deep | er |    |    |    |    |    |    |

- [x] Iteración 1: $\text{getReg(t1 := deep * 4)}$

Se obtienen los registro `R1`, `R1` y `R2` dado que se carga `deep` en `R1` y `4` en `R2`. Como deep no es usalo a futuro se almacena el valor de la multiplicacion `t1` en `R1`.

| R1 | R2 | R3 |$\|$| we | have | to | go | deep | er | t1 | t2 | t3 | t4 | t5 | t6 |
|----|----|----|----|----|------|----|----|------|----|----|----|----|----|----|----|
| t1 | 4  |    |$\|$| we | have | to | go | deep | er | R1 |    |    |    |    |    |

Código generado: $\begin{array}{l} \text{LD R1, deep} \\ \text{LD R2, 4} \\ \text{MUL R1, R1, R2} \end{array}$

- [x] Iteración 2: $\text{getReg(t2 := go[t1])}$

Se obtienen los registros `R1` y `R3` dado que en R1 está el valor de `t1` y `R3` es un registro vacío.

| R1 | R2 | R3 |$\|$| we | have | to | go | deep | er | t1 | t2 | t3 | t4 | t5 | t6 |
|----|----|----|----|----|------|----|----|------|----|----|----|----|----|----|----|
| t1 | 4  | t2 |$\|$| we | have | to | go | deep | er | R1 | R3 |    |    |    |    |

Código generado: $\begin{array}{l} \text{LD R3, go(R1)} \end{array}$

- [x] Iteración 3: $\text{getReg(t3 := t2 + er)}$

Se obtienen los registro `R1`, `R3` y `R1` dado que en `R3` esta el valor de `t2` y carga `er` en `R1` porque `t1` no se usa luego. Como `er` no es utulizado a futuro se almacena el valor de la suma `t3` en `R1`.

| R1 | R2 | R3 |$\|$| we | have | to | go | deep | er | t1 | t2 | t3 | t4 | t5 | t6 |
|----|----|----|----|----|------|----|----|------|----|----|----|----|----|----|----|
| t3 | 4  | t2 |$\|$| we | have | to | go | deep | er |    | R3 | R1 |    |    |    |

Código generado: $\begin{array}{l} \text{LD R1, er} \\ \text{ADD R1, R3, R1} \end{array}$

- [x] Iteración 4: $\text{getReg(t4 := t3 * 4)}$

Se obtienen los registro `R1`, `R2` y `R1` dado que en `R2` esta el valor `4` y en `R1` está el valor de `t3`. Como `t3` no es utilizado a futuro se almacena el valor de la multiplicacion `t4` en `R1`.

| R1 | R2 | R3 |$\|$| we | have | to | go | deep | er | t1 | t2 | t3 | t4 | t5 | t6 |
|----|----|----|----|----|------|----|----|------|----|----|----|----|----|----|----|
| t4 | 4  | t2 |$\|$| we | have | to | go | deep | er |    | R3 |    | R1 |    |    |

Código generado: $\begin{array}{l} \text{MUL R1, R1, R2} \end{array}$

- [x] Iteración 5: $\text{getReg(t5 := to[t4])}$

Se obtienen los registros `R1` y `R3` dado que en `R1` está el valor de `t4`. Como `t2` no es utilizado a futuro se almacena el valor de `t5` en `R3`.

| R1 | R2 | R3 |$\|$| we | have | to | go | deep | er | t1 | t2 | t3 | t4 | t5 | t6 |
|----|----|----|----|----|------|----|----|------|----|----|----|----|----|----|----|
| t4 | 4  | t5 |$\|$| we | have | to | go | deep | er |    |    |    | R1 | R3 |    |

Código generado: $\begin{array}{l} \text{LD R3, to(R1)} \end{array}$

- [x] Iteración 6: $\text{getReg(t6 := have * 4)}$

Se obtienen los registro `R1`, `R2` y `R2` dado que en `R2` esta el valor `4` y carga a `R1` la variable `have` dado que `t4` ya no se usará a futuro. Como `4` no es utilizado a futuro se almacena el valor de `t6` en `R2`.

| R1 | R2 | R3 |$\|$| we | have   | to | go | deep | er | t1 | t2 | t3 | t4 | t5 | t6 |
|----|----|----|----|----|--------|----|----|------|----|----|----|----|----|----|----|
|have| t6 | t5 |$\|$| we |have, R1| to | go | deep | er |    |    |    |    | R3 | R2 |

Código generado: $\begin{array}{l} \text{LD R1, have} \\ \text{MUL R2, R1, R2} \end{array}$

- [X] Iteración 7: $\text{getReg(we[t6] := t5)}$

Se obtienen los registros `R2` y `R3` dado que en `R2` esta el valor de `t6` y en `R3` esta el valor de `t5`. 

| R1 | R2 | R3 |$\|$| we | have   | to | go | deep | er | t1 | t2 | t3 | t4 | t5 | t6 |
|----|----|----|----|----|--------|----|----|------|----|----|----|----|----|----|----|
|have| t6 | t5 |$\|$| we |have, R1| to | go | deep | er |    |    |    |    | R3 | R2 |

Código generado: $\begin{array}{l} \text{ST we(R2), R3} \end{array}$

Finalmente obtenemos que 

$$
\begin{array}{l} 
\text{LD R1, deep} \\
\text{LD R2, 4} \\
\text{MUL R1, R1, R2} \\
\text{ } \\
\text{LD R3, go(R1)} \\
\text{ } \\
\text{LD R1, er} \\ 
\text{ADD R1, R3, R1} \\
\text{ } \\
\text{MUL R1, R1, R2} \\
\text{ } \\
\text{LD R3, to(R1)} \\
\text{ } \\
\text{LD R1, have} \\ 
\text{MUL R2, R1, R2} \\
\text{ } \\
\text{ST we(R2), R3}
\end{array}
$$

## Pregunta 4

### Parte (4.a)

Se planteaeel siguiente pseudo-código

$$
\begin{array}{l}
\text{n = number} \\
\text{count = 0} \\
\text{while (n != 1) do} \\
~~~~~~~~\text{if (n\%2 == 2) do} \\
~~~~~~~~~~~~~~~~\text{n = n/2} \\
~~~~~~~~~~~~~~~~\text{count++} \\
~~~~~~~~\text{else do} \\
~~~~~~~~~~~~~~~~\text{n = 3*n + 1} \\
~~~~~~~~~~~~~~~~\text{count++} \\
\text{print(count)} \\
\end{array}
$$

### Parte (4.b)

El TAC asociado es el siguiente

$$
\begin{array}{l}
\text{~ 1 : n := number} \\
\text{~ 2 : count := 0} \\
\text{~ 3 : if n == 1 goto (13)} \\
\text{~ 4 : t1 := n\%2} \\
\text{~ 5 : if t1 != 0 goto (9)} \\
\text{~ 6 : count := count + 1} \\
\text{~ 7 : n := n/2} \\
\text{~ 8 : goto (3)} \\
\text{~ 9 : count := count + 1} \\
\text{10 : t2 := 3*n} \\
\text{11 : n := t2 + 1} \\
\text{12 : goto (3)} \\
\text{13 : print count} \\
\end{array}
$$

### Parte (4.c)

### Parte (4.d)
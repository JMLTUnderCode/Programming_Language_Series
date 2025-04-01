# Resolución de Tarea 4 - Generacion de Código Intermedio (Fecha: 02-04-2025)

$$
\begin{matrix}
\text{Universidad Simón Bolívar} \\
\text{Departamento de Computación y Tecnología de la Información} \\
\text{CI4721 - Lenguajes de Programación II} \\
\text{Enero - Marzo 2025} \\
\text{Estudiante: Junior Miguel Lara Torres (17-10303)} \\
\text{ } \\
\Large \text{Tarea 4 (10 puntos)} \\
\end{matrix}
$$

>[!IMPORTANT]
> Para una correcta visualización de la tarea es recomendable clonar el repositorio y usar una extensión que admita Markdown + Latex complejo (Ej. [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)), dado que durante la resolución de la tarea se usa latex que el motor Markdown de Github no soporta.

# Indice#
- [Resolución de Tarea 4 - Generacion de Código Intermedio (Fecha: 02-04-2025)](#resolución-de-tarea-4---generacion-de-código-intermedio-fecha-02-04-2025)
- [Indice#](#indice)
- [Pregutna 1](#pregutna-1)
	- [Parte (1.a)](#parte-1a)
	- [Parte (1.b)](#parte-1b)
	- [Parte (1.c)](#parte-1c)
	- [Parte (1.d)](#parte-1d)
- [Pregunta 2](#pregunta-2)
	- [Parte (2.a)](#parte-2a)
	- [Parte (2.b)](#parte-2b)
- [Pregunta 3](#pregunta-3)

# Pregutna 1

## Parte (1.a)

Bajo la idea de la implementacion del $not$ y $or$ vistos en clase, con el uso del teorema $a \implies b \equiv \neg a \vee b$ queda que la representación intermedia para $B \to B \implies B$ es

$$
\begin{array}{rcl}
B_0 &  \to & B_1 \implies B_2 ~\{\\
    &      & ~~~~~~~~B_1.false \leftarrow B_0.true \\
	&      & ~~~~~~~~B_1.true \leftarrow newLabel() \\
	&      & ~~~~~~~~B_2.true \leftarrow B_0.true \\
	&      & ~~~~~~~~B_2.false \leftarrow B_0.false \\
	&      & ~~~~~~~~B_0.code \leftarrow concat(B_1.code, label(B_1.true), B_2.code) \\
    &      & \} 
\end{array}
$$

## Parte (1.b)

Tomando la ampliación con $M$

$$
\begin{array}{rcl}
B &  \to & B \implies MB \\
M   & \to  & \lambda \\
\end{array}
$$

Y tomando como guía la implementación vista en clase para $not$ y $or$ queda que

$$
\begin{array}{rcl}
B_0 &  \to & B_1 \implies MB_2 ~\{\\
    &      & ~~~~~~~~backpatch(B_1.truelist, M.instr) \\
	&      & ~~~~~~~~B_0.truelist \leftarrow merge(B_1.falselist, B_2.truelist) \\
	&      & ~~~~~~~~B_0.falselist \leftarrow B_2.falselist \\
    &      & \} \\
M   & \to  & \lambda ~\{ M.instr = nextInstr \} \\
\end{array}
$$

## Parte (1.c)

Se tiene la siguiente implementación para $S$

$$
\begin{array}{rcl}
S_0 &  \to & while~~B_1 : S_1~\&~B_2 : S_2 ~\{\\
    &      & ~~~~~~~~begin \leftarrow newLabel() \\
	&      & ~~~~~~~~B_1.true \leftarrow newLabel() \\
	&      & ~~~~~~~~B_1.false \leftarrow newLabel() \\
	&      & ~~~~~~~~S_1.next \leftarrow begin \\
	&      & ~~~~~~~~B_2.true \leftarrow newLabel() \\
	&      & ~~~~~~~~B_2.false \leftarrow S_0.next \\
	&      & ~~~~~~~~S_2.next \leftarrow begin \\
	&      & ~~~~~~~~S_0.code \leftarrow concat( \\
	&      & ~~~~~~~~~~~~~~~~label(begin), \\
	&      & ~~~~~~~~~~~~~~~~B_1.code \\
	&      & ~~~~~~~~~~~~~~~~label(B_1.true) \\
	&      & ~~~~~~~~~~~~~~~~S_1.code \\
	&      & ~~~~~~~~~~~~~~~~gen('goto'~begin) \\
	&      & ~~~~~~~~~~~~~~~~label(B_1.false) \\
	&      & ~~~~~~~~~~~~~~~~B_2.code \\
	&      & ~~~~~~~~~~~~~~~~label(B_2.true) \\
	&      & ~~~~~~~~~~~~~~~~S_2.code \\
	&      & ~~~~~~~~~~~~~~~~gen('goto'~begin) \\
	&      & ~~~~~~~~ ) \\
    &      & \} \\
\end{array}
$$

## Parte (1.d)

Usando la misma idea vistas en los apartados anteriores, se expande con $M$ y $N$.

$$
\begin{array}{rcl}
S &  \to & while~~M~B~M : S~N~\&~M~B~M : S \\
M & \to  & \lambda \\
N & \to  & \lambda \\
\end{array}
$$

Ahora se tiene la siguiente implementación de $S$

$$
\begin{array}{rcl}
S_0 &  \to & while~~M_1B_1M_2 : S_1N~\&~M_3B_2M_4 : S_2 ~\{\\
    &      & ~~~~~~~~backpatch(B_1.truelist, M_2.instr) \\
	&      & ~~~~~~~~backpatch(B_1.falselist, M_3.instr) \\
	&      & ~~~~~~~~backpatch(S_1.nextlist, M_1.instr) \\
	&      & ~~~~~~~~backpatch(N.nextlist, M_1.instr) \\
	&      & ~~~~~~~~backpatch(B_2.truelist, M_4.instr) \\
	&      & ~~~~~~~~backpatch(S_2.nextlist, M_1.instr) \\
	&      & ~~~~~~~~S.nextlist \leftarrow B_2.falselist \\
	&      & ~~~~~~~~gen('goto'~~M_1.instr) \\
    &      & \} \\
M   & \to  & \lambda ~\{ M.instr = nextInstr ~\} \\
N   & \to  & \lambda ~\{ \\
	&      & ~~~~~~~~N.nextlist \leftarrow makelist(nextlist) \\
	&      & ~~~~~~~~gen('goto~\_') \\
	&      & \}
\end{array}
$$

# Pregunta 2

Planteando la implementacion para el $while$ tenemos

$$
\begin{array}{rcl}
S   & \to  & while ~\{\\
    &      & ~~~~~~~~loop \leftarrow newLabel() \\
	&      & ~~~~~~~~emit('label', loop) \\
    &      & \}~ E ~\{\\
    &      & ~~~~~~~~out \leftarrow newLabel() \\
	&      & ~~~~~~~~emit('gofalse', out) \\
    &      & \}~ do~~S ~\{\\
    &      & ~~~~~~~~emit('goto', loop) \\
	&      & ~~~~~~~~emit('label', out) \\
    &      & \} \\
\end{array}
$$

Sin embargo, se considera que la producción del estilo $S \to id, id = E, E;$ es una secuencia de asignaciones.

Por otro lado, teniendo en cuenta que se quiere procesar la siguientes instrucciones

$$
\begin{array}{l}
	s, i = 0, 0; \\
	while (i < 10) do \\
	~~~~~~ s, i = s + (i*i) / 2, i + 1;
\end{array}
$$

Obtenemos la siguiente cadena de producciones asociadas

$$
\begin{array}{rcl}
S   &  \to & S ; S \\
	&   |  & id = E; S \\
	&   |  & s = E; S \\
	&   |  & s = n; S \\
	&   |  & s = 0; S \\
	&   |  & s = 0; S; S \\
	&   |  & s = 0; id = E; S \\
	&   |  & s = 0; i = E; S \\
	&   |  & s = 0; i = n; S \\
	&   |  & s = 0; i = 0; S \\
	&   |  & s = 0; i = 0; while~~E~~do~~S \\
	&   |  & s = 0; i = 0; while~~(E)~~do~~S \\
	&   |  & s = 0; i = 0; while~~(E < E)~~do~~S \\
	&   |  & s = 0; i = 0; while~~(id < E)~~do~~S \\
	&   |  & s = 0; i = 0; while~~(i < E)~~do~~S \\
	&   |  & s = 0; i = 0; while~~(i < n)~~do~~S \\	
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~S; S \\	
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~id = E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = E + E; S \\	
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = id + E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + E/E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (E)/E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (E*E)/E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (id*E)/E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*E)/E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*id)/E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*i)/E; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*i)/n; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*i)/2; S \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*i)/2; id = E \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*i)/2; i = E \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*i)/2; i = E + E \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*i)/2; i = id + E \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*i)/2; i = i + E \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*i)/2; i = i + n \\
	&   |  & s = 0; i = 0; while~~(i < 10)~~do~~s = s + (i*i)/2; i = i + 1 \\
\end{array}
$$

## Parte (2.a)

Nos queda el siguiente código de máquina de pila

| Stack       |
|:------------|
| push 0      |
| lvalue s    |
| assign      |
| push 0      |
| lvalue i    |
| assign      |
| loop        |
| rvalue i    |
| push 10     |
| lt          |
| gofalse out |
| rvalue s    |
| rvalue i    |
| rvalue i    |
| mult        |
| push 2      |
| div         |
| add         |
| lvalue s    |
| assign      | 
| rvalue i    |
| push 1      |
| add         |
| lvalue i    |
| assign      |
| goto loop   |
| out         |

## Parte (2.b)

El código de tres direcciones queda que

| Code                   |
|:-----------------------|
| s := 0                 |
| i := 0                 |
| begin                  |
| if i < 10 goto loop    |
| goto out               |
| loop                   |
| t2 := i * i            |
| t3 := t2 / 2           |
| t4 := s + t3           |
| s := t4                |
| t5 := i + 1            |
| i := t5                |
| goto begin             |
| out                    |

# Pregunta 3

![alt text](9patqj.gif)

![alt text](Imagen3.png)

>[!NOTE]
> Comparta el contenido de la pregunta 3 a su antojo.
> 
> PD: Primero fue la imagen del progreso del proyecto, luego se me ocurrió el GIF ganstar. Asi que subí los dos xd.
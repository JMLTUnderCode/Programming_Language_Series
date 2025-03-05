# Resolución de Tarea 2 - Gramáticas de Operadores y Traducción Dirigida por Sintaxis (Fecha: 06-03-2025)

$$
\begin{matrix}
\text{Universidad Simón Bolívar} \\
\text{Departamento de Computación y Tecnología de la Información} \\
\text{CI4721 - Lenguajes de Programación II} \\
\text{Enero - Marzo 2025} \\
\text{Estudiante: Junior Miguel Lara Torres (17-10303)} \\
\text{ } \\
\Large \text{Tarea 2 (10 puntos)} \\
\end{matrix}
$$

# Indice
- [Resolución de Tarea 2 - Gramáticas de Operadores y Traducción Dirigida por Sintaxis (Fecha: 06-03-2025)](#resolución-de-tarea-2---gramáticas-de-operadores-y-traducción-dirigida-por-sintaxis-fecha-06-03-2025)
- [Indice](#indice)
	- [Pregunta 1](#pregunta-1)
		- [Parte (1.a)](#parte-1a)
		- [Parte (1.b)](#parte-1b)
	- [Pregunta 2](#pregunta-2)


## Pregunta 1
Dada la gramática $\large IFT = (\text{\\{} n, +, if, then, else \text{\\}}, \text{\\{} E \text{\\}}, P, E)$ con $P$ formado por:

$$
\begin{array}{ccl}
E & \rightarrow & if~\~E~\~then~\~E~\~else~\~E \\
  &  |  & if~\~E~\~then~\~E \\
  &  |  & E~\~+~\~E \\
  &  |  & n 
\end{array}
$$

### Parte (1.a)

La gramatica aumentada queda

$$
\begin{array}{ccll}
E_0 & \rightarrow & if~\~E_1~\~then~\~E_2~\~else~\~E_3 & \{~E_0.val \leftarrow E_1.val~~?~~ E_2.val : E_3.val~\} \\
  &  |  & if~\~E_1~\~then~\~E_2 & \{~E_0.val \leftarrow E_1.val~\~?~\~ E_2.val : 0~\}\\
  &  |  & E_1~\~+~\~E_2 & \{~E_0.va; \leftarrow E_1.val + E_2.val~\}\\
  &  |  & n & \{~E_0.val \leftarrow n.val~\}
\end{array}
$$

>[!NOTE]
> * El "Código interno" de las producciones esta escrito como ternarias de C++.
> * El valor 0 para la segunda producción es un valor por defecto para el caso en que la condición sea falsa.

### Parte (1.b)

Separando la parte de suma y la parte de condicional, para asi
eliminar prefijos comunes de una mejor forma, queda que

$$
\begin{array}{ccl}
E  & \rightarrow & if~\~E~\~then~\~E~\~E' \\
   &  |  & S \\
E' &  |  & else~\~E \\
   &  |  & \lambda \\
S  &  \rightarrow & S~\~+~\~S \\
   &  |  & n 
\end{array}
$$

Eliminamos recursión a izquierda de S, queda que

$$
\begin{array}{ccl}
E  & \rightarrow & if~\~E~\~then~\~E~\~E' \\
   &  |  & S \\
E' & \rightarrow & else\~~E \\
   &  |  & \lambda \\
S  & \rightarrow & N~S'\\
S' & \rightarrow & +NS'\\
   &  |  & \lambda \\
N  & \rightarrow & E \\
   &  |  & n
\end{array}
$$

Ahora su representación como gramática de atributo con
`val` de tipo sintetizado e `in` de tipo heredado:

$$
\begin{array}{ccll}
E_0 & \rightarrow & if~\~E_1~\~then~\~E_2~\~E' & \{~ E_0.val \leftarrow E_1.val~\~?~\~ E_2.val : E'.val~\}\\
   &  |  & S & \{~ E_0.val \leftarrow S.val~\}\\ \\

E' & \rightarrow & else~\~E & \{~ E'.val \leftarrow E.val~\}\\
   &  |  & \lambda & \{~ E'.val \leftarrow 0 ~\} \\ \\

S  & \rightarrow & N~S' & \left\{\begin{array}{l} S'.in \leftarrow N.val \\ S.val \leftarrow S'.val \end{array}\right\}\\ \\

S'_0 & \rightarrow & +NS'_1& \left\{\begin{array}{l} S'_1.in \leftarrow S'_0.in + N.val \\ S'_0.val \leftarrow S'_1.val \end{array} \right\}\\
   &  |  & \lambda & \{~ S'_0.val \leftarrow S'_0.in ~\}\\ \\

N  & \rightarrow & E & \{~ N.val \leftarrow E.val ~\}\\
   &  |  & n & \{~ N.val \leftarrow n.val ~\}
\end{array}
$$

## Pregunta 2




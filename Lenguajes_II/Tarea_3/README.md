# Resolución de Tarea 3 - Verificación de Tipos (Fecha: 19-03-2025)

$$
\begin{matrix}
\text{Universidad Simón Bolívar} \\
\text{Departamento de Computación y Tecnología de la Información} \\
\text{CI4721 - Lenguajes de Programación II} \\
\text{Enero - Marzo 2025} \\
\text{Estudiante: Junior Miguel Lara Torres (17-10303)} \\
\text{ } \\
\Large \text{Tarea 3 (10 puntos)} \\
\end{matrix}
$$

>[!IMPORTANT]
> Para una correcta visualización de la tarea es recomendable clonar el repositorio y usar una extensión que admita Markdown + Latex complejo (Ej. [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)), dado que durante la resolución de la tarea se usa latex que el motor Markdown de Github no soporta.

# Indice
- [Resolución de Tarea 3 - Verificación de Tipos (Fecha: 19-03-2025)](#resolución-de-tarea-3---verificación-de-tipos-fecha-19-03-2025)
- [Indice](#indice)
- [Pregunta 1](#pregunta-1)
	- [Parte (1.a)](#parte-1a)
	- [Parte (1.b)](#parte-1b)
- [Pregunta 2](#pregunta-2)
- [Pregunta 3](#pregunta-3)
	- [Parte (3.a)](#parte-3a)
	- [Parte (3.b)](#parte-3b)
	- [Parte (3.c)](#parte-3c)
	- [Parte (3.d)](#parte-3d)

# Pregunta 1
Dada las siguientes declaraciones de tipos

```Crystal
type pokemon = struct
	pi : float
	ka : pokebola
	chu : pokebola
end
```

```Crystal
type pokebola = *pokemon
```

## Parte (1.a)
El grafo de tipos asociado queda como

![Grafo](<pregunta_1a.png>)

## Parte (1.b)
Dado el siguiente conjunto de declaraciones
```go
var a : pokemon
var b = &a : Tb 
var c = (*b).chu : Tc 
var d = (*a.chu).pi
var e = *(*(*c).ka).chu
```

* `a` se puede ver directo como tipo `pokemon`.

* `b` recibe la dirección de memoria de `a`. Como `a` es de tipo `pokemon`, `b` resulta ser de tipo `*pokemon` (un puntero a pokemon).

* `c` se asigna con `(*b).chu`. Como `b` apunta a un `struct pokemon`, al acceder a `.chu` se obtiene un elemento de tipo `pokebola`. Por lo tanto, `c` es de tipo `pokebola`.

* `d` se asigna con `(*a.chu).pi`. Aquí, `a.chu` es de tipo `pokebola` (un alias para `*pokemon`), y al desreferenciarlo `(*a.chu)` se accede a un `struct pokemon`. Luego, `.pi` accede a un elemento de tipo `float`, por lo que `d` es de tipo `float`.
  
* `e` se asigna con `*(*(*c).ka).chu`. Primero, `c` (de tipo `pokebola`) se desreferencia para acceder a un `struct pokemon`. Luego, se accede a `ka` (de tipo `pokebola`), se desreferencia nuevamente y se accede a `chu`, que también es de tipo `pokebola`. Finalmente, al desreferenciar `chu`, se obtiene un `struct pokemon`, por lo que `e` es de tipo `pokemon`.

Finalmente, a nivel de grafo tenemos
![Grafo variables](pregunta_1b.png)

# Pregunta 2

Dado los siguiente símbolos con su tipos (potencialmente polimórficos):
$$
\begin{array}{rcl}
\text{cmap} & : & \beta \\
\text{f}  & : & \gamma \\
\text{x}  & : & \rho \\
\text{[]}  & : & \forall \alpha.list(\alpha) \\
\text{null} & : & \forall \alpha.list(\alpha) \to bool \\
\text{head} & : & \forall \alpha.list(\alpha) \to \alpha \\
\text{tail} & : & \forall \alpha.list(\alpha) \to list(\alpha) \\
\text{if} & : & \forall \alpha.bool \times \alpha \times \alpha \to list(\alpha) \\
\text{concat} & : & \forall \alpha.list(\alpha) \to list(\alpha) \to list(\alpha) \\
\text{match} & : & \forall \alpha.\alpha \times \alpha \to list(\alpha) \\
\end{array}
$$

Considere también la siguiente expresión:

$$\text{match(cmap(f, x), if(null(x), [], concat(f(head(x)), cmap(f, tail(x)))))}$$

# Pregunta 3


## Parte (3.a)


## Parte (3.b)


## Parte (3.c)


## Parte (3.d)


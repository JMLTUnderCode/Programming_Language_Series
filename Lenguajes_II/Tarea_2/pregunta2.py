# Universidad Simón Bolívar
# Departamento de Computación y Tecnología de la Información
# CI4721 - Lenguajes de Programación II
# Prof. Ricardo Monascal
# Enero - Marzo 2025
# Estudiante: Junior Miguel Lara Torres (17-10303)

import re
from textwrap import fill

# Estructuras de datos para almacenar la gramática y las precedencias
#GRAMMAR = {}
GRAMMAR = {
	'E': [['E', '+', 'E'], ['E', '*', 'E'], ['id']],
}
#INITIAL_SYMBOL = None
INITIAL_SYMBOL = 'E'
#PRECEDENCES = {}
PRECEDENCES = {
	('id', '+'): '>',
    ('id', '*'): '>',
    ('id', '$'): '>',

    ('+', 'id'): '<',
    ('+', '+'): '>',
    ('+', '*'): '<',
    ('+', '$'): '>',

    ('*', 'id'): '<',
    ('*', '+'): '>',
    ('*', '*'): '>',
    ('*', '$'): '>',

    ('$', 'id'): '<',
    ('$', '+'): '<',
    ('$', '*'): '<',
}

SPECIAL_SYMBOL = '$'
BUILD_STATUS = False
#TERMINALS = [SPECIAL_SYMBOL]
TERMINALS = ['id', '+', '*', SPECIAL_SYMBOL]
WIDTH = 90

# Funcion de predecencias
F = {}
G = {}

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()
            self.edges[node] = set()

    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            self.edges[from_node].add(to_node)

    def __str__(self):
        result = "Graph:\n"
        for node in self.nodes:
            result += f"{node}: {', '.join(self.edges[node])}\n"
        return result

GRAPH = Graph()

def longest_path(graph, start_node):
    visited = set()
    stack = []
    distances = {node: float('-inf') for node in graph.nodes}
    distances[start_node] = 0

    def topological_sort(node):
        visited.add(node)
        for neighbor in graph.edges[node]:
            if neighbor not in visited:
                topological_sort(neighbor)
        stack.append(node)

    for node in graph.nodes:
        if node not in visited:
            topological_sort(node)

    while stack:
        node = stack.pop()
        if distances[node] != float('-inf'):
            for neighbor in graph.edges[node]:
                if distances[neighbor] < distances[node] + 1:
                    distances[neighbor] = distances[node] + 1

    return distances

def build_graph():
    global GRAPH, F, G

    # Agregar nodos para cada terminal
    for terminal in TERMINALS:
        GRAPH.add_node('f' + terminal)
        GRAPH.add_node('g' + terminal)

    # Agregar aristas según las precedencias
    for (t1, t2), op in PRECEDENCES.items():
        if op == '<':
            GRAPH.add_edge('g' + t2, 'f' + t1)
        elif op == '>':
            GRAPH.add_edge('f' + t1, 'g' + t2)

    # Calcular los caminos más largos para F y G
    for terminal in TERMINALS:
        f_node = 'f' + terminal
        g_node = 'g' + terminal
        F[terminal] = max(longest_path(GRAPH, f_node).values())
        G[terminal] = max(longest_path(GRAPH, g_node).values())

    print(GRAPH)

# Función para enmarcar y justificar texto
def print_framed(texto, type=1, just='l'):
	if (type): # 1 = Sin prompt
		lineas = texto.split('\n')
		for linea in lineas:
			for sublinea in fill(linea, WIDTH).split('\n'):
				if (just == 'l'):
					print('| ' + sublinea.ljust(WIDTH - (4 if "Reduce: " not in sublinea else -5)) + ' |')
				else:
					print('| ' + sublinea.center(WIDTH - (4 if "Reduce: " not in sublinea else -5)) + ' |')
		return

    # Con prompt
	lineas = texto.split('\n')
	for linea in lineas:
		for sublinea in fill(linea, WIDTH).split('\n'):
			if (just == 'l'):
				print('|\\.~ ' + sublinea.ljust(WIDTH-7) + ' |')
			else:
				print('|\\.~ ' + sublinea.center(WIDTH-7) + ' |')

# Función para imprimir toda la gramática
def print_grammar():
	grammar_text = "\nGramática:\n"
	if not GRAMMAR:
		grammar_text += "*La gramática está vacía*\n"
	else:
		if not INITIAL_SYMBOL:
			grammar_text += "*No hay símbolo inicial definido*\n"
		else:
			grammar_text += f"Símbolo inicial: {INITIAL_SYMBOL}\n"
		for non_terminal, productions in GRAMMAR.items():
			first = True
			for symbols in productions:
				production = ' '.join(symbols) if symbols else 'λ'
				if first:
					grammar_text += f"{non_terminal} -> {production}\n"
					first = False
				else:
					grammar_text +=  len(non_terminal)*" " + f"  | {production}\n"

	grammar_text += "\nPrecedencias:\n"
	if not PRECEDENCES:
		grammar_text += "*No hay precedencias definidas*\n"
	else:
		for (terminal1, terminal2), op in PRECEDENCES.items():
			if op == '>':
				op_text = "mayor"
			elif op == '<':
				op_text = "menor"
			elif op == '=':
				op_text = "igual"
			grammar_text += f"'{terminal1}' tiene {op_text} precedencia que '{terminal2}'\n"
	print_framed(grammar_text)

# Funcion para verificar gramática de operadores
def is_grammar_operators(non_terminal, symbols):
	for i in range(len(symbols) - 1):
		if symbols[i].isupper() and symbols[i + 1].isupper():
			print_framed(f"ERROR: Regla \"{non_terminal} -> {' '.join(symbols)}\" no corresponde a una gramática de operadores")
			return False

	if len(symbols) == 0 and non_terminal != INITIAL_SYMBOL:
		print_framed("Error: Sólo el símbolo inicial puede definir lambda producciones.")
		if INITIAL_SYMBOL is None:
			print_framed("Error: No se ha definido símbolo inicial.")
			return False
		else:
			return False
		
	return True

# Función para manejar la acción RULE
def handle_rule(action):
	parts = action.split()
	if len(parts) < 2:
		print_framed("Error: Acción RULE inválida.")
		return

	non_terminal = parts[1]
	if not non_terminal.isupper() or len(non_terminal) != 1:
		print_framed(f"Error: El símbolo '{non_terminal}' del lado izquierdo no es un no-terminal válido.")
		return
	
	symbols = parts[2:]
	for symbol in symbols:
		if (len(symbol) > 1 and any(c.isupper() or c.isnumeric() for c in symbol)) or symbol.isnumeric() or symbol == SPECIAL_SYMBOL:
			print_framed(f"ERROR: Regla \"{non_terminal} -> {' '.join(symbols)}\" contiene símbolos inválidos.")
			return
	
    # Verificar que no haya dos no-terminales consecutivos sin operadores entre ellos
	if not is_grammar_operators(non_terminal, symbols):
		return

	if non_terminal not in GRAMMAR:
		GRAMMAR[non_terminal] = []
	GRAMMAR[non_terminal].append(symbols)

	# Agregar símbolos terminales a la lista TERMINALS
	for symbol in symbols:
		if symbol.islower() or symbol in "+-*/()!@#%^&*()_+=[]{}|;:',.<>?/~`":
			if symbol not in TERMINALS:
				TERMINALS.append(symbol)
                
	print_framed(f"Regla añadida: {non_terminal} -> {' '.join(symbols) if symbols else 'λ'}")

# Función para manejar la acción INIT
def handle_init(action):
    parts = action.split()
    if len(parts) != 2:
        print_framed("Error: Acción INIT inválida.")
        return
    non_terminal = parts[1]
    if not non_terminal.isupper() or len(non_terminal) != 1:
        print_framed(f"ERROR: \"{non_terminal}\" no es un símbolo no-terminal")
        return
    global INITIAL_SYMBOL
    INITIAL_SYMBOL = non_terminal
    print_framed(f"\"{INITIAL_SYMBOL}\" es ahora el símbolo inicial de la gramática")


# Función para manejar la acción PREC
def handle_prec(action):
	status = True
	parts = action.split()
	if len(parts) != 4:
		print_framed("Error: Acción PREC inválida.")
		return
	
	terminal1, op, terminal2 = parts[1], parts[2], parts[3]
	if terminal1 not in TERMINALS:
		print_framed(f"Error: \"{terminal1}\" no es un símbolo terminal de la gramática.")
		status = False
	
	if terminal2 not in TERMINALS:
		print_framed(f"Error: \"{terminal2}\" no es un símbolo terminal de la gramática.")
		status = False
	
	if op not in "<>=":
		print_framed("Error: Operador inválido.")
		return
	
	if status:
		PRECEDENCES[(terminal1, terminal2)] = op
		if op == '>':
			op_text = "mayor"
		elif op == '<':
			op_text = "menor"
		elif op == '=':
			op_text = "igual"
		print_framed(f"\"{terminal1}\" tiene {op_text} precedencia que \"{terminal2}\"")


# Funcion para manejar la accion BUILD
def handle_build():
    if not GRAMMAR:
        print_framed("Error: La gramática está vacía. No se puede construir el analizador sintáctico.")
        return
	
    if not INITIAL_SYMBOL:
        print_framed("Error: No se ha especificado el símbolo inicial de la gramática.")

    build_graph()

    f_text = "Analizador sintactico construido.\nValores para F:\n"
    for terminal, value in F.items():
        f_text += f"   {terminal}: {value}\n"
    
    g_text = "Valores para G:\n"
    for terminal, value in G.items():
        g_text += f"   {terminal}: {value}\n"
    
    print_framed(f_text + "\n" + g_text)
    global BUILD_STATUS
    BUILD_STATUS= True

def handle_parse(action):
    if not BUILD_STATUS:
        print_framed("Error: ERROR: Aun no se ha construido el analizador sintactico")
        return
    
    parts = action.split(maxsplit=1)
    if len(parts) < 2:
        print_framed("Error: No se proporcionó una palabra a parsear.")
        return
    
    word = parts[1]

    # Utilizar una expresión regular para dividir la palabra en símbolos
    symbols = re.findall(r'[a-z]+|[^\s]', word)

    # Validar que la palabra solo contenga terminales válidos
    for symbol in symbols:
        if symbol.isupper():
            print_framed(f"Error: El símbolo '{symbol}' no es un terminal válido.")
            return
        if symbol == SPECIAL_SYMBOL:
            print_framed(f"Error: El símbolo '{SPECIAL_SYMBOL}' es un símbolo especial y no puede ser usado en la palabra a parsear.")
            return
        if symbol not in TERMINALS:
            print_framed(f"Error: El símbolo '{symbol}' no está definido en la gramática.")
            return

    # Construir la frase según las precedencias
    entrada = [SPECIAL_SYMBOL] + symbols + [SPECIAL_SYMBOL]
    entrada_con_precedencias = [entrada[0]]
    for i in range(len(entrada) - 1):
        entrada_con_precedencias.append(PRECEDENCES[(entrada[i], entrada[i + 1])])
        entrada_con_precedencias.append(entrada[i + 1])

    # Inicializar la pila y el punto
    pila = []
    point = 2
    start_reduce = 0
    end_reduce = 0
    width_pila = len(''.join(entrada))
    width_entrada = len(' '.join(entrada_con_precedencias)) + 2
    action = ""
    print_framed("Stack".center(width_pila+1) + '|' + "Input".center(width_entrada+2) + '|' + "Action".center(WIDTH-width_entrada-width_pila-3))
    # Función para imprimir el estado actual
    def imprimir_estado():
        pila_str = ' '.join(pila)
        pila_str += (width_pila - len(pila_str)) * ' '
    
        # Construir la cadena de entrada con precedencias resaltando la subcadena
        entrada_str = ' '.join(entrada_con_precedencias[:point] + ['.'] + entrada_con_precedencias[point:])
        if action.startswith("Reduce"):
            entrada_str = ' '.join(entrada_con_precedencias[:end_reduce]) + ' \033[92m' + ' '.join(entrada_con_precedencias[end_reduce:start_reduce+1]) + '\033[0m ' + '.' + ' '.join(entrada_con_precedencias[start_reduce+1:])
            entrada_str += (width_entrada - len(entrada_str)+9) * ' '
            print_framed(f"{pila_str} | {entrada_str} | {action}")
            return
            
        entrada_str += (width_entrada - len(entrada_str)) * ' '
        print_framed(f"{pila_str} | {entrada_str} | {action}")

    # Función para reducir según la gramática
    def reducir():
        nonlocal point, start_reduce, end_reduce, entrada_con_precedencias, pila, action
        start_point = point-1
        if (start_point > -1):
            if entrada_con_precedencias[start_point] == '>':
                end_point = start_point - 1
                while entrada_con_precedencias[end_point] != '<':
                    end_point -= 1
                subcadena = entrada_con_precedencias[end_point + 1: start_point]

                for nt, producciones in GRAMMAR.items():
                    for produccion in producciones:
                        for symbol in subcadena:
                            if symbol in produccion:
                                start_reduce = start_point
                                end_reduce = end_point
                                action = f"Reduce: {nt} -> " + ' '.join(produccion)
                                imprimir_estado()

                                # Actualizar la pila
                                for _ in produccion:
                                    pila.pop()
                                pila.append(nt)

                                # Actualizar la relación de precedencia en entrada_con_precedencias
                                if entrada_con_precedencias[end_point - 1] == entrada_con_precedencias[start_point + 1] == SPECIAL_SYMBOL:
                                    action = "Accept"
                                    entrada_con_precedencias[end_point:start_point+1] = []
                                    point = end_point
                                    imprimir_estado()
                                    return True
								
                                point = end_point+1                                
                                entrada_con_precedencias[end_point:start_point+1] = [PRECEDENCES[(entrada_con_precedencias[end_point - 1], entrada_con_precedencias[start_point + 1])]]
                                return True
        return False

    # Proceso de parseo
    #imprimir_estado()
    while True:    
        if point >= len(entrada_con_precedencias):
            print_framed("Error: Punto fuera de rango.")
            break
        if entrada_con_precedencias[point-1] == SPECIAL_SYMBOL and len(pila) == 1 and pila[0] == INITIAL_SYMBOL:
            break
        elif entrada_con_precedencias[point-1] == SPECIAL_SYMBOL and len(pila) == 1 and pila[0] != INITIAL_SYMBOL:
            print_framed("Error: Simbolo final en pila es distinto a simbolo inicial.")
        elif entrada_con_precedencias[point-1] == '<':
            action = "Shift"
            imprimir_estado()
            if entrada_con_precedencias[point] in TERMINALS:
                pila.append(entrada_con_precedencias[point])
            point += 2
        elif entrada_con_precedencias[point-1] == '>':
            if not reducir():
                print_framed("Error: No se puede reducir.")
                break
        else:
            print_framed("Error: Símbolo desconocido.")
            break

# Bucle principal
def main():
	while True:
		action = input("|\\.~ ")
		if action.startswith("RULE") or action.startswith("rule"):
			handle_rule(action)
		elif action.startswith("INIT") or action.startswith("init"):
			handle_init(action)
		elif action.startswith("PREC") or action.startswith("prec"):
			handle_prec(action)
		elif action.startswith("BUILD") or action.startswith("build"):
			handle_build()
		elif action.startswith("PARSE") or action.startswith("parse"):
			handle_parse(action)
		elif action.startswith("EXIT") or action.startswith("exit"):
			print_framed("Done")
			break
		elif action.startswith("SHOW") or action.startswith("show"):
			print_grammar()
		else:
			print_framed("Error: Acción desconocida.")

if __name__ == "__main__":
	print('+' + '-' * (WIDTH - 2) + '+')
	acciones_disponibles = """******************************\n*    Acciones disponibles    *\n************                            ***********\n* RULE <non-terminal> [<symbol> <symbol> ...]     *\n* INIT <non-terminal>                             *\n* PREC <terminal> <op> <terminal>                 *\n* BUILD                                           *\n* PARSE <string>                                  *\n* SHOW                                            *\n* EXIT                                            *\n*                                                 *\n* -> Note: Minúsculas admitidas para acciones.    *\n***************************************************\n
    """
	print_framed(acciones_disponibles, 1, 'c')
	main()
	print('+' + '-' * (WIDTH - 2) + '+')
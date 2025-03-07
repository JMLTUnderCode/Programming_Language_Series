# Universidad Simón Bolívar
# Departamento de Computación y Tecnología de la Información
# CI4721 - Lenguajes de Programación II
# Prof. Ricardo Monascal
# Enero - Marzo 2025
# Estudiante: Junior Miguel Lara Torres (17-10303)

import re
from textwrap import fill

# Estructuras de datos para almacenar la gramática y las precedencias
GRAMMAR = {}
INITIAL_SYMBOL = None
PRECEDENCES = {}
SPECIAL_SYMBOL = '$'
BUILD_STATUS = False
TERMINALS = [SPECIAL_SYMBOL]
WIDTH = 115

# Funcion de predecencias
F = {}
G = {}

# Estructura grafo para calculo de funciones de precedencias F y G.
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

# Función para calcular el camino más largo en un grafo dirigido acíclico.
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

# Función para construir el grafo de precedencias y calcular las funciones F y G.
def build_graph():
    global GRAPH, F, G

	# Determinamos las clases de equivalencia de los nodos.
    equivalence_classes = {}
    for terminal in TERMINALS:
        equivalence_classes[terminal] = {terminal}

    for (t1, t2), op in PRECEDENCES.items():
        if op == '=':
            if t1 in equivalence_classes and t2 in equivalence_classes:
                equivalence_classes[t1].update(equivalence_classes[t2])
                for t in equivalence_classes[t2]:
                    equivalence_classes[t] = equivalence_classes[t1]
            else:
                print_framed(f"Error: Los símbolos '{t1}' o '{t2}' no están definidos en las clases de equivalencia.")

    unique_classes = {frozenset(eq) for eq in equivalence_classes.values()}
    class_map = {t: eq for eq in unique_classes for t in eq}

	## Agregamos los nodos segun sus clases de equivalencias.
    for eq_class in unique_classes:
        node = ''.join(sorted(eq_class))
        GRAPH.add_node('f' + node)
        GRAPH.add_node('g' + node)

	# Agregamos los arcos entre nodos según las precedencias.
    for (t1, t2), op in PRECEDENCES.items():
        if op in ('<', '>'):
            from_node = ''.join(sorted(class_map[t1]))
            to_node = ''.join(sorted(class_map[t2]))
            if op == '<':
                GRAPH.add_edge('g' + to_node, 'f' + from_node)
            elif op == '>':
                GRAPH.add_edge('f' + from_node, 'g' + to_node)

    # Verificar ciclos en el grafo.
    def has_cycle(graph):
        visited = set()
        rec_stack = set()

        def cycle_util(node):
            if node not in visited:
                visited.add(node)
                rec_stack.add(node)
                for neighbor in graph.edges[node]:
                    if neighbor not in visited and cycle_util(neighbor):
                        return True
                    elif neighbor in rec_stack:
                        return True
                rec_stack.remove(node)
            return False

        for node in graph.nodes:
            if cycle_util(node):
                return True
        return False
    
    if has_cycle(GRAPH):
        print_framed("Error: El grafo contiene ciclos. No es posible construir el analizador sintáctico.")
        return False
    
    # Calcular los caminos más largos para F y G.
    for terminal in TERMINALS:
        f_node = 'f' + terminal
        g_node = 'g' + terminal
        F[terminal] = max(longest_path(GRAPH, f_node).values())
        G[terminal] = max(longest_path(GRAPH, g_node).values())

    #print(GRAPH)
    return True

# Función para enmarcar y justificar texto
def print_framed(text, type=1, just='l'):
	if (type): # 1 = Sin prompt
		lines = text.split('\n')
		for line in lines:
			if line.find("Reduce") != -1:
				print('| ' + line + (WIDTH - len(line) + 19)*' ' + ' |')
				return
			for subline in fill(line, WIDTH).split('\n'):
				if (just == 'l'):
					print('| ' + subline.ljust(WIDTH - 4) + ' |')
				else:
					print('| ' + subline.center(WIDTH - 4) + ' |')
		return

    # Con prompt
	lines = text.split('\n')
	for line in lines:
		for subline in fill(line, WIDTH).split('\n'):
			if (just == 'l'):
				print('|\\.~ ' + subline.ljust(WIDTH-7) + ' |')
			else:
				print('|\\.~ ' + subline.center(WIDTH-7) + ' |')

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

# Funcion para verificar gramática de operadores.
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

# Función para manejar la acción RULE.
def handle_rule(action):
	global GRAMMAR
      
	# Verificamos la cantidad de argumentos.
	parts = action.split()
	if len(parts) < 2:
		print_framed("Error: Acción RULE inválida.")
		return

	# Verificamos que el no-terminal sea un solo caracter y mayúscula.
	non_terminal = parts[1]
	if not non_terminal.isupper() or len(non_terminal) != 1:
		print_framed(f"Error: El símbolo '{non_terminal}' del lado izquierdo no es un no-terminal válido.")
		return
	
	# Verificamos que la regla tenga simbolos validos.
	symbols = parts[2:]
	for symbol in symbols:
		if (len(symbol) > 1 and any(c.isupper() or c.isnumeric() for c in symbol)) or symbol.isnumeric() or symbol == SPECIAL_SYMBOL:
			print_framed(f"ERROR: Regla \"{non_terminal} -> {' '.join(symbols)}\" contiene símbolos inválidos.")
			return
	
    # Verificar que no haya dos no-terminales consecutivos sin operadores entre ellos
	if not is_grammar_operators(non_terminal, symbols):
		return

	# Agregamos la regla a la gramática.
	if non_terminal not in GRAMMAR:
		GRAMMAR[non_terminal] = []
	GRAMMAR[non_terminal].append(symbols)

	# Agregar símbolos terminales a la lista TERMINALS
	for symbol in symbols:
		if symbol.islower() or symbol in "+-*/()!@#%^&*()_+=[]{}|;:',.<>?/~`":
			if symbol not in TERMINALS:
				TERMINALS.append(symbol)
                
	print_framed(f"Regla añadida: {non_terminal} -> {' '.join(symbols) if symbols else 'λ'}")

# Función para manejar la acción INIT.
def handle_init(action):
    global INITIAL_SYMBOL
    
	# Verificamos la cantidad de argumentos.
    parts = action.split()
    if len(parts) != 2:
        print_framed("Error: Acción INIT inválida.")
        return
    
	# Verificamos que el no-terminal sea un solo caracter y mayúscula.
    non_terminal = parts[1]
    if not non_terminal.isupper() or len(non_terminal) != 1:
        print_framed(f"ERROR: \"{non_terminal}\" no es un símbolo no-terminal")
        return
    
    INITIAL_SYMBOL = non_terminal
    print_framed(f"\"{INITIAL_SYMBOL}\" es ahora el símbolo inicial de la gramática")


# Función para manejar la acción PREC.
def handle_prec(action):
	global PRECEDENCES
	status = True
      
	# Verificamos la cantidad de argumentos.
	parts = action.split()
	if len(parts) != 4:
		print_framed("Error: Acción PREC inválida.")
		return
	
	# Verificamos que los símbolos sean terminales existenten en la gramatica.
	terminal1, op, terminal2 = parts[1], parts[2], parts[3]
	if terminal1 not in TERMINALS:
		print_framed(f"Error: \"{terminal1}\" no es un símbolo terminal de la gramática.")
		status = False
	
	if terminal2 not in TERMINALS:
		print_framed(f"Error: \"{terminal2}\" no es un símbolo terminal de la gramática.")
		status = False
	
	# Verificar operador valido.
	if op not in "<>=":
		print_framed("Error: Operador inválido.")
		return
	
	# Guardamos precedencias.
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
    global BUILD_STATUS
    
	# Verificamos contruccion de gramatica.
    if not GRAMMAR:
        print_framed("Error: La gramática está vacía. No se puede construir el analizador sintáctico.")
        return
	
    if not INITIAL_SYMBOL:
        print_framed("Error: No se ha especificado el símbolo inicial de la gramática.")

    BUILD_STATUS= True
    # Verificacion construccion del grafo.
    if not build_graph():
        return
    
	# Mostramos F y G.
    f_text = "Analizador sintactico construido.\nValores para F:\n"
    for terminal, value in F.items():
        f_text += f"   {terminal}: {value}\n"
    
    g_text = "Valores para G:\n"
    for terminal, value in G.items():
        g_text += f"   {terminal}: {value}\n"
    
    print_framed(f_text + "\n" + g_text)

def handle_parse(action):
    # Verificamos estados de construccion.
    if not BUILD_STATUS:
        print_framed("Error: ERROR: Aun no se ha construido el analizador sintactico")
        return
    
	# Verificamos argumentos.
    parts = action.split(maxsplit=1)
    if len(parts) < 2:
        print_framed("Error: No se proporcionó una palabra a parsear.")
        return
    
	# Utilizar una expresión regular para dividir la palabra en símbolos
    phrase = parts[1]
    symbols = re.findall(r'[a-z]+|[^\s]', phrase)

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

    # Construir la frase según las precedencias.
    input_phrase = [SPECIAL_SYMBOL] + symbols + [SPECIAL_SYMBOL]
    input_with_precedences = [input_phrase[0]]
    for i in range(len(input_phrase) - 1):
        input_with_precedences.append(PRECEDENCES[(input_phrase[i], input_phrase[i + 1])])
        input_with_precedences.append(input_phrase[i + 1])

    # Inicializacion de variables.
    stack = []
    point = 2
    start_reduce = 0
    end_reduce = 0
    width_stack = len(' '.join(input_phrase)) - 5
    width_entrance = len(' '.join(input_with_precedences)) + 2
    action = ""
    print_framed("Stack".center(width_stack+1) + '|' + "Input".center(width_entrance+2) + '|' + "Action".center(WIDTH-width_entrance-width_stack-7))
    
	# Función para imprimir el estado actual del parseo.
    def show_state():
        stack_str = ' '.join(stack)
        stack_str += (width_stack - len(stack_str)) * ' '
    
        # Construir la cadena de entrada con precedencias resaltando la subcadena
        input_phrase_str = ' '.join(input_with_precedences[:point] + ['.'] + input_with_precedences[point:])
        if action.startswith("Reduce"):
            input_phrase_str = ' '.join(input_with_precedences[:end_reduce]) + ' \033[38;5;82m\033[5m' + ' '.join(input_with_precedences[end_reduce:start_reduce+1]) + '\033[25m\033[0m ' + '.' + ' '.join(input_with_precedences[start_reduce+1:])
            input_phrase_str += (width_entrance - len(input_phrase_str)+23)*' '
            print_framed(f"{stack_str} | {input_phrase_str} | {action}")
            return
            
        input_phrase_str += (width_entrance - len(input_phrase_str))*' '
        print_framed(f"{stack_str} | {input_phrase_str} | {action}")

    # Función para reducir según la gramática
    def reduce():
        nonlocal point, start_reduce, end_reduce, input_with_precedences, stack, action
        start_point = point-1
        if (start_point > -1):
            if input_with_precedences[start_point] == '>':
                end_point = start_point - 1
                while input_with_precedences[end_point] != '<':
                    end_point -= 1
                substring = input_with_precedences[end_point + 1: start_point]

                for non_term, productions in GRAMMAR.items():
                    for production in productions:
                        for symbol in substring:
                            if symbol in production:
                                start_reduce = start_point
                                end_reduce = end_point

                                # Actualizar la pila y verificar si se puede reducir.
                                aux_stack = stack.copy()
                                for k in range(len(production)-1, -1, -1):
                                    if aux_stack[-1] == production[k]:
                                        aux_stack.pop()
                                    else:
                                        action = f"Decline, cannot be reduced by {non_term} -> " + ' '.join(production)
                                        show_state()
                                        return False
                                    
                                action = f"Reduce: {non_term} -> " + ' '.join(production)
                                show_state()
                                stack = aux_stack.copy()
                                stack.append(non_term)

                                # Verificar caso borde, el final cuando se tiene [$ $]
                                if input_with_precedences[end_point - 1] == input_with_precedences[start_point + 1] == SPECIAL_SYMBOL:
                                    action = "Accept"
                                    input_with_precedences[end_point:start_point+1] = []
                                    point = end_point
                                    show_state()
                                    return True
                                
								# Actualizar la relación de precedencia en entrada_con_precedencias
                                point = end_point+1                            
                                input_with_precedences[end_point:start_point+1] = [PRECEDENCES[(input_with_precedences[end_point - 1], input_with_precedences[start_point + 1])]]
                                return True
        return False

    # Proceso de parseo
    status = True
    while status:
        # Verificamos borde maximo de la frase con precedencias.    
        if point >= len(input_with_precedences):
            print_framed("Error: Punto fuera de rango.")
            break
        
        # Verificamos estapa final de parseo.
        if input_with_precedences[point-1] == SPECIAL_SYMBOL and len(stack) == 1 and stack[0] == INITIAL_SYMBOL:
            break
        
        # Verificamos si en la etapa final el ultimo simbolo no terminal no es el inicial.
        elif input_with_precedences[point-1] == SPECIAL_SYMBOL and len(stack) == 1 and stack[0] != INITIAL_SYMBOL:
            print_framed("Error: Simbolo final en pila es distinto a simbolo inicial.")
            
		# Realizamos shift.
        elif input_with_precedences[point-1] == '<' or input_with_precedences[point-1] == '=':
            action = "Shift"
            show_state()
            if input_with_precedences[point] in TERMINALS:
                stack.append(input_with_precedences[point])
            point += 2
            
		# Realizamos reduce.
        elif input_with_precedences[point-1] == '>':
            status = reduce()
            
        else:
            print_framed("Error: Símbolo desconocido.")
            break

# Manejados principal de acciones.
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
	print(f"|                                          ******************************                                         |")
	print(f"|                                          *    {'\033[4;49;5m'}Acciones disponibles{'\033[0m'}    *                                         |")
	acciones_disponibles = f"""************                            ***********\n* RULE <non-terminal> [<symbol> <symbol> ...]     *\n* INIT <non-terminal>                             *\n* PREC <terminal> <op> <terminal>                 *\n* BUILD                                           *\n* PARSE <string>                                  *\n* SHOW                                            *\n* EXIT                                            *\n*                                                 *\n* -> Note: Minúsculas admitidas para acciones.    *\n***************************************************\n
    """
	print_framed(acciones_disponibles, 1, 'c')
	main()
	print('+' + '-' * (WIDTH - 2) + '+')
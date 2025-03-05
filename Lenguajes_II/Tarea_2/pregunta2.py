from textwrap import fill

# Estructuras de datos para almacenar la gramática y las precedencias
grammar = {}
initial_symbol = None
precedences = {}
ancho = 90

# Función para enmarcar y justificar texto
def print_enmarcado(texto, type=1, just='l'):
	if (type): # 1 = Sin prompt
		lineas = texto.split('\n')
		for linea in lineas:
			for sublinea in fill(linea, ancho).split('\n'):
				if (just == 'l'):
					print('| ' + sublinea.ljust(ancho-4) + ' |')
				else:
					print('| ' + sublinea.center(ancho-4) + ' |')
		return

    # Con prompt
	lineas = texto.split('\n')
	for linea in lineas:
		for sublinea in fill(linea, ancho).split('\n'):
			if (just == 'l'):
				print('|\\.~ ' + sublinea.ljust(ancho-7) + ' |')
			else:
				print('|\\.~ ' + sublinea.center(ancho-7) + ' |')

# Función para imprimir toda la gramática
def print_grammar():
	grammar_text = ""
	if not grammar:
		print_enmarcado("La gramática está vacía.")
	else:
		grammar_text = "Gramática:\n"
		for non_terminal, productions in grammar.items():
			first = True
			for symbols in productions:
				production = ' '.join(symbols) if symbols else 'λ'
				if first:
					grammar_text += f"{non_terminal} -> {production}\n"
					first = False
				else:
					grammar_text +=  len(non_terminal)*" " + f"  | {production}\n"

	grammar_text += "\nPrecedencias:\n"
	for (terminal1, terminal2), op in precedences.items():
		if op == '>':
			op_text = "tiene mayor"
		elif op == '<':
			op_text = "tiene menor"
		elif op == '=':
			op_text = "tiene igual"
		grammar_text += f"'{terminal1}' {op_text} precedencia que '{terminal2}'\n"
	print_enmarcado(grammar_text)

# Función para manejar la acción RULE
def handle_rule(action):
    parts = action.split()
    if len(parts) < 2:
        print_enmarcado("Error: Acción RULE inválida.")
        return
    non_terminal = parts[1]
    if not non_terminal.isupper() or len(non_terminal) != 1:
        print_enmarcado("Error: El símbolo del lado izquierdo no es un no-terminal válido.")
        return
    symbols = parts[2:]
    if not all(symbol.islower() or symbol.isupper() or symbol in "+-*/()$" for symbol in symbols):
        print_enmarcado("Error: La regla contiene símbolos inválidos.")
        return
    if not all(symbol.islower() or symbol.isupper() or symbol in "+-*/()" for symbol in symbols):
        print_enmarcado(f"ERROR: Regla \"{non_terminal} -> {' '.join(symbols)}\" no corresponde a una gramatica de operadores")
        return

	# Verificar que no haya dos no-terminales consecutivos sin operadores entre ellos
    for i in range(len(symbols) - 1):
        if symbols[i].isupper() and symbols[i + 1].isupper():
            print_enmarcado(f"ERROR: Regla \"{non_terminal} -> {' '.join(symbols)}\" no corresponde a una gramatica de operadores")
            return

    if non_terminal not in grammar:
        grammar[non_terminal] = []
    grammar[non_terminal].append(symbols)
    print_enmarcado(f"Regla añadida: {non_terminal} -> {' '.join(symbols) if symbols else 'λ'}")


# Función para manejar la acción INIT
def handle_init(action):
    parts = action.split()
    if len(parts) != 2:
        print_enmarcado("Error: Acción INIT inválida.")
        return
    non_terminal = parts[1]
    if not non_terminal.isupper() or len(non_terminal) != 1:
        print_enmarcado(f"ERROR: \"{non_terminal}\" no es un simbolo no-terminal")
        return
    global initial_symbol
    initial_symbol = non_terminal
    print_enmarcado(f"\"{initial_symbol}\" es ahora el simbolo inicial de la gramatica")


# Función para manejar la acción PREC
def handle_prec(action):
    parts = action.split()
    if len(parts) != 4:
        print_enmarcado("Error: Acción PREC inválida.")
        return
    terminal1, op, terminal2 = parts[1], parts[2], parts[3]
    if terminal1 not in "+-*/()$" or terminal2 not in "+-*/()$":
        print_enmarcado("Error: Los símbolos involucrados no son terminales válidos.")
        return
    if op not in "<>=":
        print_enmarcado("Error: Operador inválido.")
        return
    precedences[(terminal1, terminal2)] = op
    if op == '>':
        op_text = "tiene mayor"
    elif op == '<':
        op_text = "tiene menor"
    elif op == '=':
        op_text = "tiene igual"
    print_enmarcado(f"\"{terminal1}\" {op_text} precedencia que \"{terminal2}\"")


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
		elif action.startswith("EXIT") or action.startswith("exit"):
			print_enmarcado("Done")
			break
		elif action.startswith("SHOW") or action.startswith("show"):
			print_grammar()
		else:
			print_enmarcado("Error: Acción desconocida.")

if __name__ == "__main__":
	print('+' + '-' * (ancho - 2) + '+')
	acciones_disponibles = """******************************\n*    Acciones disponibles    *\n************                            ***********\n* RULE <non-terminal> [<symbol> <symbol> ...]     *\n* INIT <non-terminal>                             *\n* PREC <terminal> <op> <terminal>                 *\n* BUILD                                           *\n* PARSE <string>                                  *\n* SHOW                                            *\n* EXIT                                            *\n*                                                 *\n* -> Note: Minúsculas admitidas para acciones.    *\n***************************************************\n
    """
	print_enmarcado(acciones_disponibles, 1, 'c')
	main()
	print('+' + '-' * (ancho - 2) + '+')
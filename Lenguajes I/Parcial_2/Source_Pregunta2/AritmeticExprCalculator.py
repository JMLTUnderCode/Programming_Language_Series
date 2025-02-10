# variable global para los operadores matematicos validos descrito en chars.
OPERATORS = ['+', '-', '*', '/']

# Clase principal para las operaciones sobre expresiones aritmeticas descritas en version PRE-ORDER y POST-ORDER.
class Operation():
    def __init__(self, expr: str) -> None:
        self.expression_data = expr
        self.stack_eval = []
        self.stack_mostrar = []
        self.expression_as_list_mostrar = self.expression_data.split(" ")
        self.expression_as_list_eval = list(map((lambda x: int(x) if x.isdigit() else x), self.expression_as_list_mostrar))
        
    # Funcion encargada de evaluar la expresion en el orden descrito.
    def EVAL(self, operation_mode: str):
        # Version Post-Order de Pre-Order
        if operation_mode.upper() == "PRE":
            self.expression_as_list_eval.reverse() # Version Post-Order de Pre
        
        # Iteramos por la cantidad de elementos de la expresion.
        for symbols in self.expression_as_list_eval:
            # Stackeamos los elementos que sean numeros.
            if type(symbols) is int:
                self.stack_eval.append(symbols)

            # Calculamos la expresion a mostrar para un elemento tipo operador.
            elif symbols in OPERATORS and len(self.stack_eval) > 1:
                # Como se invirtio inicialmente para el caso PRE y manejarlo como una version POST,
                # entonces se debe operar de manera original.
                if operation_mode.upper() == "PRE":
                    result = operating(self.stack_eval[-1], symbols, self.stack_eval[-2])

                # Operamos para version POST.
                if operation_mode.upper() == "POST":
                    result = operating(self.stack_eval[-2], symbols, self.stack_eval[-1])

                # Se hace pop mediante el cut de lista (:) y se push el resultado.
                self.stack_eval = self.stack_eval[:-2]
                self.stack_eval.append(result)

            # Caso de error para cuando la expresion no esta correctamente escrita en el orden dado.   
            else:
                print("*      -> ERROR 404 <-                                                       *")
                print(f"*         La expresion dada no corresponde a un orden {operation_mode.upper()}FIJO.             *")
                return False
        return True

    # Funcion encargada de mostrar la expresion en el orden descrito.
    def MOSTRAR(self, operation_mode: str):
        # Version Post-Order de Pre-Order
        if operation_mode.upper() == "PRE":
            self.expression_as_list_mostrar.reverse() 
        
        # Iteramos por la cantidad de elementos de la expresion.
        for symbols in self.expression_as_list_mostrar:
            # Stackeamos los elementos que sean numeros.
            if symbols.isdigit():
                self.stack_mostrar.append(symbols)

            # Calculamos la expresion a mostrar para un elemento tipo operador.
            elif symbols in OPERATORS and len(self.stack_mostrar) > 1:
                last_element = self.stack_mostrar[-1]
                second_last_element = self.stack_mostrar[-2]
                
                # Caso cuando la subexpresion de la derecha contiene un + o - y se tiene un * o / a operar,
                # entonces incluimos parentesis.
                if (symbols == "*" or symbols == "/") and ("+" in last_element or "-" in last_element):
                    last_element = f"({last_element})"

                # Caso cuando la subexpresion de la izquierda contiene un + o - y se tiene un * o / a operar,
                # entonces incluimos parentesis.
                if (symbols == "*" or symbols == "/") and ("+" in second_last_element or "-" in second_last_element):
                    second_last_element = f"({second_last_element})"

                # Como se invirtio inicialmente para el caso PRE y manejarlo como una version POST,
                # entonces se debe operar de manera original.
                if operation_mode.upper() == "PRE":
                    result = f"{last_element} {symbols} {second_last_element}"

                # Operamos para version POST.
                if operation_mode.upper() == "POST":
                    result = f"{second_last_element} {symbols} {last_element}"

                # Se hace pop mediante el cut de lista (:) y se push el resultado.
                self.stack_mostrar = self.stack_mostrar[:-2]
                self.stack_mostrar.append(result)
            
            # Caso de error para cuando la expresion no esta correctamente escrita en el orden dado.
            else:
                print("*      -> ERROR 404 <-                                                       *")
                print(f"*         La expresion dada no corresponde a un orden {operation_mode.upper()}FIJO.             *")
                return False
        return True

# Funcion que dado dos numeros y un char representativo a un operador matematico (+,-,* y /) realiza 
# el calculo matematico perse. 
def operating (a:int, op:str, b:int):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a//b

# Funcion que permite verificar para un char(simbolo) si este NO ES operador matematico (+,-,* y /) o un numero.
def is_Not_Symbol_Expression(symbol: str):
    return not(symbol.isdigit() or symbol in OPERATORS)

# Funcion que permite verificar si el string dado NO REPRESENTA ser el string "PRE" o "POST" indicando los ordenes
# de evaluacion PREFIJO y POSTFIJO.
def is_Not_Evaluation_Order(prefix: str):
    status = not(prefix == "PRE" or prefix.upper() == "POST")
    if status:
        print("*      -> ERROR 401 <-                                                       *")
        print("*         Orden de evaluacion invalido. Inserte HELP para ver comandos.      *")
    return status

# Funcion que permite verificar si el string dado NO ES una correcta expresion aritmetica, pasando por un chequeo
# de numeros no negativos, operadores matematicos (+,-,* y /) validos y la condicion para expresiones aritmeticas
# que consta de verificar la (cantidad de operadores matematicos - 1 == cantidad de numeros a operar).
def is_Not_Correct_Expression(expr: str):
    expr = expr.split(" ")
    # Verificar que sean operadores o numeros.
    if not(all(list(map((lambda x: x.isdigit() or x in OPERATORS), expr)))):
        print("*      -> ERROR 402 <-                                                       *")
        print("*         Simbolos invalidos en la expresion.                                *")
        print("*         Elementos admitidos:                                               *")
        print("*             - Operadores Suma(+), Resta(-), Multiplicar(*) y Dividir(/).   *")
        print("*             - Numero enteros no-negativos.                                 *")
        print("*             - No usar los operadores como prefijo ni postfijo (-4 o 4-).   *")
        print("*             - Cada elemento de la expresion debe ser separado por espacio. *")
        print("*                 Ej. \"+ * + 3 4 5 7\", \"8 3 - 8 4 4 + * +\"               *")

        return True

    # Condicional esencial para las expresiones aritmeticas. 
    amount_of_numbers = sum(list(map((lambda x: 1 if x.isdigit() else 0), expr)))
    amount_of_operators = sum(list(map((lambda x: 1 if x in OPERATORS else 0), expr)))

    if amount_of_operators + 1 != amount_of_numbers:
        print("*      -> ERROR 403 <-                                                       *")
        print("*         La cantidad de operadores y numeros es incongruentes.              *")
        return True
    return False


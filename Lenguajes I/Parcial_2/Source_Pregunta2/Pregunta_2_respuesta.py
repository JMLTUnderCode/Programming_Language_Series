#
#   Universidad Simon Bolivar
#   Departamento de Computación y Tecnología de la Información
#   CI3641 – Lenguajes de Programación 1
#   Trimestre: Septiembre - Diciembre 2023
#   Profesor: Ricardo Monascal
#   Estudiante: Junior Miguel Lara Torres
#   Carnet: 17-10303
#
#   Parcial 2 - Pregunta 2
#
#   "Se desea que modele e implemente, en el lenguaje de su elección, 
#     un programa que maneje expresiones aritmáticas sobre enteros."
#
#   La solucion planteada consta de crear un modulo-libreria con la clase "Operation"
#   que manejara la evaluacion y el mostrado de las expresiones aritmeticas. 
#   Para facilitar ambas funciones se piensa en la estrategia de que una expresion
#   PRE-ORDER puede, mediante un reverse/swap de la expresion, convertirse en una
#   expresion POST-ORDER, de este forma no importa en qué caso estemos siempre operamos
#   en version POST-ORDER, claro esta que para el caso de tener PRE-ORDER y trabajar en su
#   version POST-ORDER hay que cuidar ciertos detalles al momento de operar, pues no es
#   lo mismo "3-4" que "4-3". Adicionalmente, la libreria tiene las funciones de verificacion
#   de datos y expresiones para mostrar mensajes de error.

from AritmeticExprCalculator import *
from itertools import takewhile, dropwhile

def main():
    print("*----------------------------------------------------------------------------*")
    print("*--------------------* ARITMETIC EXPRESSION CALCULATOR *---------------------*")
    print("*                                                                            *")
    print("*    OPERACIONES DISPONIBLES:                                                *")
    print("*      -- EVAL <orden> <expr>:                                               *")
    print("*         + <orden>:                                                         *")
    print("*             PRE: Que representa expresiones escritas en orden pre–fijo.    *")
    print("*             POST: Que representa expresiones escritas en orden post–fijo.  *")
    print("*      -- MOSTRAR <orden> <expr>:                                            *")
    print("*             Muestra en pantalla una expresion identificada con el orden.   *")
    print("*      -- SALIR                                                              *")
    print("*             Finaliza el programa.                                          *")

    while(True):
        # Lectura por pantalla del comando.
        print("*                                                                            *")
        command = input("* ~/ >> ")

        # Extraemos solo los comandos, EVAL, MOSTRAR, SALIR, PRE y POST. Luego parametrizamos.
        extracting_commands = "".join(list(takewhile(is_Not_Symbol_Expression, command)))
        parameters = extracting_commands.split(" ")

        if parameters[0].upper() == "SALIR":
            break

        # Extraemos la expresion matematica a calcular. Se almacena de una vez en la clase.
        extracting_expression = "".join(list(dropwhile(is_Not_Symbol_Expression, command)))

        # Verificamos que las expresion tenga los simbolos correctos.
        if is_Not_Correct_Expression(extracting_expression):
            continue

        expr = Operation(extracting_expression)

        # Analizamos los casos para cada comando.
        if parameters[0].upper() == "EVAL":
            if is_Not_Evaluation_Order(parameters[1]):
                continue
            
            # Procedemos a analizar y evaluar la expresion.
            if expr.EVAL(parameters[1]):
                result = expr.stack_eval[0]
                print(f"* ~/ >> = {result}" + (" "*(67-len(str(result))) + "*"))

        elif parameters[0].upper() == "MOSTRAR":
            if is_Not_Evaluation_Order(parameters[1]):
                continue
            
            # Procedemos a analizar y mostrar la expresion.
            if expr.MOSTRAR(parameters[1]):
                result = expr.stack_mostrar[0]
                print(f"* ~/ >> = {result}" + (" "*(67-len(result)) + "*"))

        elif parameters[0].upper() == "HELP":
            print("*    **-> Comandos Permitidos <-**                                           *")
            print("*      -- EVAL <orden> <expr>:                                               *")
            print("*         + <orden>:                                                         *")
            print("*             PRE: Que representa expresiones escritas en orden pre–fijo.    *")
            print("*             POST: Que representa expresiones escritas en orden post–fijo.  *")
            print("*      -- MOSTRAR <orden> <expr>:                                            *")
            print("*             Muestra en pantalla una expresion identificada con el orden.   *")
            print("*      -- SALIR                                                              *")
            print("*             Finaliza el programa.                                          *")
            print("*    Se permiten sus respectivas versiones en minusculas.                    *")
            print("*                                                                            *")

        else:
            print("*      -> ERROR 400 <-                                                       *")
            print("*         Comando principal invalido. Inserte HELP para ver comandos.        *")

if __name__=="__main__":
    main()
#
#   Universidad Simon Bolivar
#   Departamento de Computación y Tecnología de la Información
#   CI3641 – Lenguajes de Programación 1
#   Trimestre: Septiembre - Diciembre 2023
#   Profesor: Ricardo Monascal
#   Estudiante: Junior Miguel Lara Torres
#   Carnet: 17-10303
#
#   Parcial 3 - Pregunta 6
#
#   "Se desea que modele e implemente, en el lenguaje de su elección, un 
#   intérprete para un subconjunto del lenguaje Prolog: (...)"
#
#   Se crean los respectivos modulos InterpreteProlog.py que simula un 
#   subconjunto del lenguaje Prolog, este se encarga de manejar las expresiones
#   soportadas, atomos, variables y estructuras permitiendo definirlas y preguntar
#   si dichas expresiones son validas y para que valores son validas.
#
#   (VERSION NO FUNCIONAL)

from InterpreteProlog import *
from collections import deque

# Funcion que permite tokenizar una cadena de caracteres. Esta permite separar
# todos aquellos predicados que forman parte de una regla general.
def split_command(string):
    result = []
    predicate = ""
    stack = []

    if ' ' not in string:
        return [string]

    for char in string:
        predicate += char
        # Guardamos comandos y hechos directos.
        if '(' not in predicate and char == " " and predicate != " ":
            result.append(predicate[:-1])
            predicate = ""

        if predicate == " ":
            predicate = ""

        if char == '(':
            stack.append(char)

        elif char == ')':
            if len(stack) > 0:
                stack = stack[:-1]
            else:
                print("Error: Unbalanced parenthesis.")

            if len(stack) == 0:
                result.append(predicate)
                predicate = ""

    if '(' not in predicate and predicate != "":
        result.append(predicate)

    if len(stack) != 0:
        print("Error: Unbalanced parenthesis.")

    return result

def main():
    print("*----------------------------------------------------------------------------*")
    print("*-----------------------------* VIRTUAL TABLE *------------------------------*")
    print("*                                                                            *")
    print("*    OPERACIONES DISPONIBLES:                                                *")
    print("*      -- DEF <expresion> [<expresion>]                                      *")
    print("*      -- ASK <expresion>                                                    *")
    print("*      -- SALIR                                                              *")
    print("*                                                                            *")

    machineProlog = Prolog()
    while True:
        # Lectura de comandos.
        command = input("* ~/ >> ")
        parameters = split_command(command)
        size_argv = len(parameters)
        print(size_argv)
        # Verificacion de salida.
        if parameters[0].upper () == "SALIR":
            break
        
        # Verificar si se quiere crear una nueva clase o subclase.
        if parameters[0].upper() == "DEF" and size_argv > 1:
            machineProlog.DEF(parameters[1:])

            error = machineProlog.ERROR_DEF
            if error != "":
                print(f"* ~/ >> -" + error + ("-" + " "*(67 - len(error))) + "*")

        # Verificar si se quiere describir una clase.
        elif parameters[0].upper() == "ASK" and size_argv == 2:
            descriptions = machineProlog.ASK(parameters[1])

            error = machineProlog.ERROR_ASK
            if error != "":
                print(f"* ~/ >> -" + error + ("-" + " "*(67 - len(error))) + "*")
                continue

            # Mostrar expresiones    
            if descriptions == []:
                print("*    true.                                                                   *")
            else:
                for it in range(0, len(descriptions)-1):
                    print(f"* ~/ >> -" + descriptions[it] + ("-" + " "*(67 - len(descriptions[it]))) + "*")
                    command = input("* ~/ >> ")
                    parameters = command.split(" ")
                    size_argv = len(parameters)

                    if size_argv == 1 and parameters[0].upper() == "ACEPTAR":
                        print("*    Consulta aceptada.                                                      *")
                        break
                    elif parameters[0].upper() != "RECHAZAR":
                        print("*    Comando errado. escriba ACEPTAR O RECHAZAR.                             *")
                        print("*    Se admite version en minusculas.                                        *")

            last_description = descriptions[len(descriptions)-1]


        # Verificar si el usuario requiere ayuda en los comandos validos.
        elif parameters[0].upper() == "HELP":
            print("*    OPERACIONES DISPONIBLES:                                                *")
            print("*      -- DEF <expresion> [<expresion>]                                      *")
            print("*      -- ASK <expresion>                                                    *")
            print("*      -- SALIR                                                              *")
            print("*    Se admite version en minusculas.                                        *")

        # Error de comandos general.
        else:
            print("*      -> ERROR 400 <-                                                       *")
            print("*         Secuencia de comando erronea o incompleta. Inserte HELP.           *") 

if __name__ == "__main__":
    main()
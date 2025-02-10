#
#   Universidad Simon Bolivar
#   Departamento de Computación y Tecnología de la Información
#   CI3641 – Lenguajes de Programación 1
#   Trimestre: Septiembre - Diciembre 2023
#   Profesor: Ricardo Monascal
#   Estudiante: Junior Miguel Lara Torres
#   Carnet: 17-10303
#
#   Parcial 1 - Pregunta 5
#
#   "Se desea que modele e implemente, en el lenguaje de su elección, 
#    un programa que simule programas, intérpretes y traductores con 
#    los vistos al estudiar los diagramas de T."
#
#   La solucion es mediante BrutForce usando diccionarios para categorizar
#   cada componente, traductor, interpreter, maquina y los lenguajes.

from DiagramT import *

def main():
    print("*----------------------------------------------------------------------------*")
    print("*--------------------------* DIAGRAM T SIMULATION *--------------------------*")
    print("*                                                                            *")
    print("*    OPERACIONES DISPONIBLES:                                                *")
    print("*      -- DEFINIR <tipo> [<argumentos>]:                                     *")
    print("*         + PROGRAMA <nombre> <lenguaje>                                     *")
    print("*         + INTERPRETE <lenguaje_base> <lenguaje>                            *")
    print("*         + TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino>   *")
    print("*      -- EJECUTABLE <nombre>                                                *")
    print("*      -- SALIR                                                              *")
    print("*                                                                            *")

    while True:
        command = input("* ~/ >> ")
        parameters = command.split(" ")

        if parameters[0].upper() == "SALIR":
            break
        
        elif parameters[0].upper() == "EJECUTABLE" and len(parameters) == 2:
            EXECUTING(parameters[1])

        elif parameters[0].upper() == "HELP":
            print("*    **-> Comandos Permitidos <-**                                           *")
            print("*      -- DEFINIR <tipo> [<argumentos>]:                                     *")
            print("*         + PROGRAMA <nombre> <lenguaje>                                     *")
            print("*         + INTERPRETE <lenguaje_base> <lenguaje>                            *")
            print("*         + TRADUCTOR <lenguaje_base> <lenguaje_origen> <lenguaje_destino>   *")
            print("*      -- EJECUTABLE <nombre>                                                *")
            print("*      -- SALIR                                                              *")
            print("*    Se permiten sus respectivas versiones en minusculas.                    *")

        elif parameters[0].upper() == "DEFINIR":
            if parameters[1].upper() == "TRADUCTOR" and len(parameters) == 5:
                ADD_TRANSTALOR(parameters[2], parameters[3], parameters[4])

            elif parameters[1].upper() == "INTERPRETE" and len(parameters) == 4:
                ADD_INTERPRETER(parameters[2], parameters[3])
            
            elif parameters[1].upper() == "PROGRAMA" and len(parameters) == 4:
                ADD_PROGRAM(parameters[2], parameters[3])

            else:
                print("*      -> ERROR 401 <-                                                       *")
                print("*         Sintaxis equivocada. Inserte HELP para ver comandos.               *")

        else:
            print("*      -> ERROR 402 <-                                                       *")
            print("*         Operacion invalida. Inserte HELP para ver comandos.                *")

if __name__=="__main__":
    main()
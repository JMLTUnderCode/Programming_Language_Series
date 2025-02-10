#
#   Universidad Simon Bolivar
#   Departamento de Computación y Tecnología de la Información
#   CI3641 – Lenguajes de Programación 1
#   Trimestre: Septiembre - Diciembre 2023
#   Profesor: Ricardo Monascal
#   Estudiante: Junior Miguel Lara Torres
#   Carnet: 17-10303
#
#   Parcial 3 - Pregunta 4
#
#   "Se desea que modele e implemente, en el lenguaje de su elección, un manejador de tablas
#   de métodos virtuales para un sistema orientado a objetos con herencia simple y despacho
#   dinámico de métodos:"
#
#   Se crea e; respectivo modulo "virtualtable.py" que contiene la clase principal
#   que simula la tabla virtual para metodos de cada clase descrita en ella.
#   Se espera que en caso de errar en definicion el usuario sepa que la clase consta
#   de su propios atributos de error. En ella se describen dos metodos importantes
#   CLASE y DESCRIBIR.
#

from virtualtable import *

def main():
    print("*----------------------------------------------------------------------------*")
    print("*-----------------------------* VIRTUAL TABLE *------------------------------*")
    print("*                                                                            *")
    print("*    OPERACIONES DISPONIBLES:                                                *")
    print("*      -- CLASS <tipo> [<nombre>]                                            *")
    print("*      -- DESCRIBIR <nombre>                                                 *")
    print("*      -- SALIR                                                              *")
    print("*                                                                            *")

    DataTable = VirtualTable()
    while True:
        # Lectura de comandos.
        command = input("* ~/ >> ")
        parameters = command.split(" ")
        size_argv = len(parameters)

        # Verificacion de salida.
        if parameters[0].upper () == "SALIR":
            break
        
        # Verificar si se quiere crear una nueva clase o subclase.
        if parameters[0].upper() == "CLASS" and size_argv > 1:
            DataTable.CLASE(parameters[1:])

            error = DataTable.ERROR_CLASS
            if error != "":
                print(f"* ~/ >> -" + error + ("-" + " "*(67 - len(error))) + "*")

        # Verificar si se quiere describir una clase.
        elif parameters[0].upper() == "DESCRIBIR" and size_argv == 2:
            descriptions = DataTable.DESCRIBIR(parameters[1])

            error = DataTable.ERROR_DESCRIBIR
            if error != "":
                print(f"* ~/ >> -" + error + ("-" + " "*(67 - len(error))) + "*")
                continue

            print(f"*        Virtual Methods Table of {parameters[1]}" + (" "*(43 - len(parameters[1]))) + "*") 
            if len(descriptions) != 0:
                for description in descriptions:
                    aux = (" "*(55 - len(description[0])*2 - len(description[1]))) + "*"
                    print(f"*             " + description[0] + " -> " + description[1] + " :: " + description[0] + aux)
            else:
                print("*           > No method has been defined <                                   *")

        # Verificar si el usuario requiere ayuda en los comandos validos.
        elif parameters[0].upper() == "HELP":
            print("*    OPERACIONES DISPONIBLES:                                                *")
            print("*      -- CLASS <tipo> [<nombre>]                                            *")
            print("*      -- DESCRIBIR <nombre>                                                 *")
            print("*      -- SALIR                                                              *")
            print("*    Se admite version en minusculas.                                        *")

        # Error de comandos general.
        else:
            print("*      -> ERROR 400 <-                                                       *")
            print("*         Secuencia de comando erronea o incompleta. Inserte HELP.           *") 

if __name__ == "__main__":
    main()
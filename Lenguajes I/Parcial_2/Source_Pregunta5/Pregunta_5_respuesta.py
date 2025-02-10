#
#   Universidad Simon Bolivar
#   Departamento de Computación y Tecnología de la Información
#   CI3641 – Lenguajes de Programación 1
#   Trimestre: Septiembre - Diciembre 2023
#   Profesor: Ricardo Monascal
#   Estudiante: Junior Miguel Lara Torres
#   Carnet: 17-10303
#
#   Parcial 2 - Pregunta 5
#
#   "Se desea que modele e implemente, en el lenguaje de su elección, 
#     un programa que simule un manejador de tipos de datos."
# 
#   Se importa la respectiva libreria del manejador de datos para el problema.
#   La solucion no va mas alla que la implementacion directa de cada concepto
#   pedido. Se usa clase para la estructura principal del manejor, usando como
#   almacenes de datos a los diccionarios y el manejo de errores de hace de forma
#   interna.

from DataDriver import *

def main():
    print("*----------------------------------------------------------------------------*")
    print("*------------------------------* DATA DRIVER *-------------------------------*")
    print("*                                                                            *")
    print("*    OPERACIONES DISPONIBLES:                                                *")
    print("*      -- ATOMICO <nombre> <representación> <alineación>                     *")
    print("*      -- STRUCT <nombre> [<tipo>]                                           *")
    print("*      -- UNION <nombre> [<tipo>]                                            *")
    print("*      -- DESCRIBIR <nombre>                                                 *")
    print("*      -- SALIR                                                              *")
    print("*                                                                            *")

    DataBase = DataDrive()
    while True:
        command = input("* ~/ >> ")
        parameters = command.split(" ")
        size_argv = len(parameters)

        if parameters[0].upper() == "SALIR":
            break
        
        if parameters[0].upper() == "ATOMICO" and size_argv == 4:
            DataBase.ATOMIC(parameters[1:])

            error = DataBase.ERROR_ATOMIC 
            if error != "":
                print(f"* ~/ >> -" + error + ("-" + " "*(67 - len(error))) + "*")

        elif parameters[0].upper() == "STRUCT" and size_argv > 2:
            DataBase.STRUCT(parameters[1:])

            error = DataBase.ERROR_STRUCT
            if error != "":
                print(f"* ~/ >> -" + error + ("-" + " "*(67 - len(error))) + "*")

        elif parameters[0].upper() == "UNION" and size_argv > 2:
            DataBase.UNION(parameters[1:])

            error = DataBase.ERROR_UNION
            if error != "":
                print(f"* ~/ >> -" + error + ("-" + " "*(67 - len(error))) + "*")

        elif parameters[0].upper() == "DESCRIBIR" and size_argv == 2:
            descriptions = DataBase.DESCRIBIR(parameters[1])

            error = DataBase.ERROR_DESCRIBIR
            if error != "":
                print(f"* ~/ >> -" + error + ("-" + " "*(67 - len(error))) + "*")
            else:
                name = parameters[1]
                print("* ~/ >> For \"" + name + ("\"" + " "*(63 - len(name))) + "*")
                print("*                         Memory          Alignment        LostMemory        *")
                iter = 1
                for dest in descriptions:
                    memory = dest[0]
                    alignment = dest[1]
                    lostMemory = dest[2]
    
                    if iter == 1:
                        version = "Unpacked: "
                    elif iter == 2:
                        version = "Packed: "
                    else:
                        version = "Optimized: "

                    iter += 1
                    string1 = "{:>10}".format(str(memory))
                    string2 = "{:>10}".format(str(alignment))
                    string3 = "{:>10}".format(str(lostMemory))
                    print(f"* ~/ >>    " +  version + (" "*(14-len(version))) + string1 + "         " + string2 + "        " + string3 + "     *")
                print("*                                                                            *")


        elif parameters[0].upper() == "HELP":
            print("*    OPERACIONES DISPONIBLES:                                                *")
            print("*      -- ATOMICO <nombre> <representación> <alineación>                     *")
            print("*      -- STRUCT <nombre> [<tipo>]                                           *")
            print("*      -- UNION <nombre> [<tipo>]                                            *")
            print("*      -- DESCRIBIR <nombre>                                                 *")
            print("*      -- SALIR                                                              *")
            print("*    Se admite version en minusculas.                                        *")

        else:
            print("*      -> ERROR 400 <-                                                       *")
            print("*         Secuencia de comando erronea o incompleta. Inserte HELP.           *") 


if __name__ == "__main__":
    main()
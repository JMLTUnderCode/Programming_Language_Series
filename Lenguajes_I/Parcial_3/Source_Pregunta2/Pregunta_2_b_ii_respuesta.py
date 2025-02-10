#
#   Universidad Simon Bolivar
#   Departamento de Computación y Tecnología de la Información
#   CI3641 – Lenguajes de Programación 1
#   Trimestre: Septiembre - Diciembre 2023
#   Profesor: Ricardo Monascal
#   Estudiante: Junior Miguel Lara Torres
#   Carnet: 17-10303
#
#   Parcial 3 - Pregunta 2.b.2
#
#   "Dado un path que representa un directorio en el sistema operativo, cuenta la
#   cantidad de archivos que están localizados en el subarbol que tiene como raíz 
#   el directorio propuesto. El proceso debe crear un thread por cada subdirectorio 
#   encontrado."
#
#   Se usa la libreria os para la funcion walk que determina las raices, directorios
#   y archivos de un directorio. Luego mediante la libreria threading se crean hilos 
#   donde creaamos uno por cada subdirectorio de tal forma que vaya contando la 
#   cantidad de archivos.
#

import os
import threading

def count_files(path):
    total_files = 1 # La carpeta raiz misma.
    for root, dirs, files in os.walk(path):
        total_files += len(files) + len(dirs)
        
        # Crear un thread por cada subdirectorio
        for d in dirs:
            thread = threading.Thread(target=count_files, args=(os.path.join(root, d),))
            thread.start()
            
    return total_files

def main():
    path = input("\n* ~/ >> Ingrese path del directorio raiz: ")
    total = count_files(path)
    print(f"* ~/ >> Total Directorios + Archivos: {total}\n")

if __name__ == "__main__":
    main()
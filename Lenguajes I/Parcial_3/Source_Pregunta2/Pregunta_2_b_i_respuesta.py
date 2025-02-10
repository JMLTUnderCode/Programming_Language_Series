#
#   Universidad Simon Bolivar
#   Departamento de Computación y Tecnología de la Información
#   CI3641 – Lenguajes de Programación 1
#   Trimestre: Septiembre - Diciembre 2023
#   Profesor: Ricardo Monascal
#   Estudiante: Junior Miguel Lara Torres
#   Carnet: 17-10303
#
#   Parcial 3 - Pregunta 2.b.1
#
#   "Dadas dos vectores del mismo tamaño (representados como un arreglo), 
#   realizar el producto punto. El cálculo debe hacerse de forma 
#   concurrente, aprovechando los mecanismos provistos en el lenguaje 
#   para ello."
#
#   Se usa la libreria Procesos de la libreria multiprocessing y colas
#   para realizar el calculo concurrente del producto escalar de dos 
#   vectores de igual tamanio. Se divide el trabajo en 2 partes, un proceso
#   se encarga de realizar la primera mitad del trabajo, es decir multiplicar
#   desde el inicio hasta la mitad de los vectores el producto escalar, luego
#   el otro proceso esta calculando el producto escalar de la mitad sobrante.
#   Al final es revisar la cola donde estan almacenados los resultados parciales
#   de cada mitad para luego sumarlos.
#

from multiprocessing import Process, Queue

# Función para calcular parte del producto punto 
def producto_punto_parcial(v1, v2, inicio, fin, q):
    suma = 0
    for i in range(inicio, fin):
        suma += v1[i] * v2[i]
    q.put(suma) 

def main():
    # Leer tamaño de los vectores
    n = int(input("\n* ~/ >> Ingrese tamaño de los vectores: "))

    # Leer vector 1  
    print("* ~/ >> Elementos del vector v1:")
    v1 = []
    for i in range(n):
        v1.append(int(input(f"* ~/ >>   v1[{i}]: ")))

    # Leer vector 2
    print("* ~/ >> Elementos del vector v2:")
    v2 = []
    for i in range(n):
        v2.append(int(input(f"* ~/ >>   v2[{i}]: ")))

    # Resultado inicial del producto punto
    resultado = 0

    # Cola para comunicar el resultado parcial
    q = Queue()

    # Se divide el trabajo en 2 partes
    mitad = n // 2
    
    # Inicio de procesos.
    p1 = Process(target=producto_punto_parcial, args=(v1, v2, 0, mitad, q))
    p2 = Process(target=producto_punto_parcial, args=(v1, v2, mitad, n, q))

    # Ejecucion de los procesos
    p1.start()
    p2.start()

    # Se espera a que terminen los procesos
    p1.join()
    p2.join()

    # Se obtienen los resultados parciales
    producto_escalar_parcial_P1 = q.get()  
    producto_escalar_parcial_P2 = q.get()

    # Se suman los resultados parciales
    producto_escalar_final = producto_escalar_parcial_P1 + producto_escalar_parcial_P2

    print(f"* ~/ >> Producto Escalar de v1.v2: {producto_escalar_final}.\n")

if __name__ == '__main__':
    main()
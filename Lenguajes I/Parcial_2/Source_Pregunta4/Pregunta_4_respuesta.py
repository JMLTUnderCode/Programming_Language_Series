#
#   Universidad Simon Bolivar
#   Departamento de Computación y Tecnología de la Información
#   CI3641 – Lenguajes de Programación 1
#   Trimestre: Septiembre - Diciembre 2023
#   Profesor: Ricardo Monascal
#   Estudiante: Junior Miguel Lara Torres
#   Carnet: 17-10303
#
#   Parcial 2 - Pregunta 4
#
#   Para los valores X = 3, Y = 0, Z = 3, se tiene que:
#
#   alpha = ((X + Y ) mod 5) + 3 = (3 mod 5) + 3 = 3 + 3 <=> alpha = 6
#   betha = ((Y + Z) mod 5) + 3 = (3 mod 5) + 3 = 3 + 3 <=> betha = 6
#
#   Por lo que se tiene la funcion F_66(n) definida como
#      {  n                                                                                       si  0 <= n < 36
#      {  F_66(n - 3) + F_66(n - 12) + F_66(n - 18) + F_66(n - 24) + F_66(n - 30) + F_66(n - 36)  si  n >= 36
# 

import time
import csv

X = 3
Y = 0
Z = 3
Alpha = ((X + Y ) % 5) + 3
Betha = ((Y + Z ) % 5) + 3

# Version recursiva para la familia de funciones F_66.
def F_66_recursive(n: int):
    if n > -1 and n < Alpha*Betha:
        return n
    elif n > Alpha*Betha - 1:
        return F_66_recursive(n - 6) + F_66_recursive(n - 12) + F_66_recursive(n - 18) + F_66_recursive(n - 24) + F_66_recursive(n - 30) + F_66_recursive(n - 36)
    else:
        print(" Error: No se admiten valores negativos. ")
        return -1

# Version recursiva de cola para la familia de funciones F_66.
def F_66_recursive_tail(n: int, iter = Alpha*Betha, acum = 0, 
         F66_30 = 30, F66_24 = 24, F66_18 = 18, F66_12 = 12, F66_6 = 6, F66_0 = 0,
         step_30 = 1, step_24 = 1, step_18 = 1, step_12 = 1, step_6 = 1, step_0 = 1, 
         tram_30 = 0, tram_24 = 0, tram_18 = 0, tram_12 = 0, tram_6 = 0, tram_0 = 0):
    
    if n > -1 and n < Alpha*Betha:
        return n
    
    elif iter == n+1:
        return acum
    
    # Caso normal, sin punto critico, se calcula el acumulador y aumenta los pasos diferenciales
    # de cada componente. Estos puntos criticos son, 41, 47, 53, ... dado que para 42, 48, 53, ...
    # tenemos la actualizacion de una componente de forma CRITICA (otro elif).
    elif (iter+1)%Betha != 0:

        acum = F66_30 + F66_24 + F66_18 + F66_12 + F66_6 + F66_0
        F66_30 += step_30 
        F66_24 += step_24
        F66_18 += step_18
        F66_12 += step_12
        F66_6  += step_6
        F66_0  += step_0

        return F_66_recursive_tail(n, iter+1, acum,
                    F66_30, F66_24, F66_18, F66_12, F66_6, F66_0,
                    step_30, step_24, step_18, step_12, step_6, step_0,
                    tram_30, tram_24, tram_18, tram_12, tram_6, tram_0)
    
    # En caso de punto critico, que es justo antes de realizar la actualizacion drastica
    # de un componente.
    elif (iter+1)%Betha == 0:

        # Calculando acumulador.
        acum = F66_30 + F66_24 + F66_18 + F66_12 + F66_6 + F66_0

        # Actualizando componentes. Se aumenta el paso diferencial de cada componente.
        # Y como estamos en el punto critico, si cada componentes es mayor al (alpha*betha - 1)
        # entonces requiere la actualizacion especial, que consta de ir añadifino los 
        # terminos trampa para cada componente desde derecha a izquierda, donde la componente
        # mas a la derecha es F66_0 y el mas izquierda es F66_30, eso proviene del orden INICIAL
        # F_66(36) = F_66(30) + F_66(24) + F_66(18) + F_66(12) + F_66(6) + F_66(0)
        F66_0 += step_0
        if F66_0 > 35:
            F66_0  = tram_0 + tram_6 + tram_12 + tram_18 + tram_24 + tram_30

        F66_6 += step_6
        if F66_6 > 35:
            F66_6  = F66_0 + tram_6 + tram_12 + tram_18 + tram_24 + tram_30

        F66_12 += step_12
        if F66_12 > 35:
            F66_12 = F66_0 + F66_6 + tram_12 + tram_18 + tram_24 + tram_30

        F66_18 += step_18
        if F66_18 > 35:
            F66_18 = F66_0 + F66_6 + F66_12 + tram_18 + tram_24 + tram_30

        F66_24 += step_24
        if F66_24 > 35:
            F66_24 = F66_0 + F66_6 + F66_12 + F66_18 + tram_24 + tram_30 

        F66_30 += step_30
        if F66_30 > 35: 
            F66_30 = F66_0 + F66_6 + F66_12 + F66_18 + F66_24 + tram_30

        # Actualizando pasos diferenciales de cada componente. Esto se realiza mediante
        # una suma previa de todos los pasos, este se coloca siempre en step30 realizando
        # un swap a derecha de cada uno de los pasos actuales.
        new_step30 = step_30 + step_24 + step_18 + step_12 + step_6 + step_0
        step_0  = step_6
        step_6  = step_12
        step_12 = step_18
        step_18 = step_24
        step_24 = step_30
        step_30 = new_step30

        return F_66_recursive_tail(n, iter+1, acum, 
                    F66_30, F66_24, F66_18, F66_12, F66_6, F66_0,
                    step_30, step_24, step_18, step_12, step_6, step_0,
                    F66_0, tram_30, tram_24, tram_18, tram_12, tram_6)

# Version iterativa de la familia de funciones F_66.
def F_66_iterative(n: int):
    dinamic_vector = [0]*(n+1)
    if n < 0:
        print(" Error: No se admiten valores negativos. ")
        return -1
    else:
        for x in range(0,n+1):
            if x > -1 and x < Alpha*Betha:
                dinamic_vector[x] = x
            else:
                dinamic_vector[x] = dinamic_vector[x - 6] + dinamic_vector[x - 12] + dinamic_vector[x - 18] + dinamic_vector[x - 24] + dinamic_vector[x - 30] + dinamic_vector[x - 36]
        return dinamic_vector[n]

# Lista de prueba para archivo csv que analiza tiempos de eficiencia.
list_test = [[40]*10, [60]*10, [80]*10, [100]*10, [120]*10, [140]*10, [160]*10, [170]*10]

def generate_csv(test_case:[[int]]):
    values = []
    headers = ["N", "Funcion Recursiva", "Funcion Recursiva de Cola", "Funcion Iterativa"]
    for inner in test_case:
        mean_time1 = mean_time2 = mean_time3 = 0
        dict_tmp = {}
        dict_tmp["N"] = inner[0]
        for n in inner:
            inicio = time.perf_counter()
            F_66_recursive(n)
            fin = time.perf_counter()
            mean_time1 += fin-inicio

            inicio = time.perf_counter()
            F_66_recursive_tail(n)
            fin = time.perf_counter()
            mean_time2 += fin-inicio

            inicio = time.perf_counter()
            F_66_iterative(n)
            fin = time.perf_counter()
            mean_time3 += fin-inicio
            
        dict_tmp["Funcion Recursiva"] = float(f"{(mean_time1/10):0.4f}")
        dict_tmp["Funcion Recursiva de Cola"] = float(f"{(mean_time2/10):0.4f}")
        dict_tmp["Funcion Iterativa"] = float(f"{(mean_time3/10):0.4f}")

        values.append(dict_tmp)
        with open('means_time_family_function.csv', mode='w') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=headers )
            writer.writeheader()

            for val in values:
                writer.writerow(val)

def main():
    print("*----------------------------------------------------------------------------*")
    print("*----------------------------* FAMILY FUNCTION *-----------------------------*")
    print("*                                                                            *")
    print("*    OPERACIONES DISPONIBLES:                                                *")
    print("*      -- Ingresar el valor n. Solo debe indicar un entero no-negativo.      *")
    print("*      -- Indique 'q' para salir.                                            *")

    while(True):
        print("*                                                                            *")
        n = input("* ~/ >> ")

        if n == 'q':
            break
        elif n.isdigit():
            N = int(n)

            # Determinamos tiempo y resultado para la version recursiva.
            inicio = time.perf_counter()
            result = F_66_recursive(N)
            fin = time.perf_counter()
            print(f"* ~/ >> F_66({N}) = {result}", end='')
            print(f"   -- Time: {(fin-inicio):0.4f} sg." + (" "*(44-len(str(result))-len(n)-len(str(f"{(fin-inicio):0.4f}"))) + "*"))             

            # Determinamos tiempo y resultado para la version recursiva de cola.
            inicio = time.perf_counter()
            result = F_66_iterative(N)
            fin = time.perf_counter()
            print(f"* ~/ >> F_66({N}) = {result}", end='')
            print(f"   -- Time: {(fin-inicio):0.4f} sg." + (" "*(44-len(str(result))-len(n)-len(str(f"{(fin-inicio):0.4f}"))) + "*"))             

            # Determinamos tiempo y resultado para la version iterativa.
            inicio = time.perf_counter()
            result = F_66_recursive_tail(N)
            fin = time.perf_counter()
            print(f"* ~/ >> F_66({N}) = {result}", end='')
            print(f"   -- Time: {(fin-inicio):0.4f} sg." + (" "*(44-len(str(result))-len(n)-len(str(f"{(fin-inicio):0.4f}"))) + "*"))             

        else:
            print("*                                                                            *")
            print("* ~/ >> ERROR: Solo indicar un entero no-negativo o 'q' para salir.          *") 

if __name__=="__main__":
    main()
    generate_csv(list_test)

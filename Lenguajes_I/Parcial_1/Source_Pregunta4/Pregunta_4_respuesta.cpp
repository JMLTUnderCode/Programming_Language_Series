/*
    Universidad Simon Bolivar
    Departamento de Computación y Tecnología de la Información
    CI3641 – Lenguajes de Programación 1
    Trimestre: Septiembre - Diciembre 2023
    Profesor: Ricardo Monascal
    Estudiante: Junior Miguel Lara Torres
    Carnet: 17-10303

    Parcial 1 - Pregunta 4

    "Se desea que modele e implemente, en el lenguaje de su elección, 
    un módulo que defina el tipo de vectores de tres (3) dimensiones 
    y operadores aritméticas sobre estos. La librería debe cumplir 
    con las siguientes características:
    Debe saber tratar las siguientes expresiones aritméticas:
        • suma: representada por el símbolo +.
        • resta: representada por el símbolo -.
        • producto cruz: representada por el símbolo *.
        • producto punto: representada por el símbolo %.
        • norma: representada por el símbolo &."
    
    Para correr este programa con total exito se debe compilar
    en la consola con la siguiente serie de comandos.

    g++ -c vector3D.cpp
    g++ -c Pregunta_4_respuesta.cpp
    g++ -o (nombre) vector3D.o Pregunta_4_respuesta.o
    ./(nombre)

    Si se quiere ver la cobertura se debe instalar gcovr y luego
    aplicas los siguientes comandos:

    g++ --coverage -c vector3D.cpp
    g++ --coverage -c Pregunta_4_respuesta.cpp
    g++ --coverage -o (nombre) vector3D.o Pregunta_4_respuesta.o
    ./(nombre)
    gcovr

    Este ejecutara en tu consola las operaciones descritas
    en el bloque main de este programa.
*/ 

#include <iostream>
#include "vector3D.h"

using namespace std;

int main(){
    // Inicializacion de vectores.
    V_3D a(-100, 0, 100);
    V_3D b(500, 1000, 3000);
    V_3D c(-500, -500, -500);
    V_3D d(-20.3, 0, 91.2);
    V_3D e; // Vector nulo

    // CASOS DE PRUEBA
    // Operaciones vector con vector.
    cout << b+c << endl;
    cout << a*d + c << endl;
    cout << (b+d)*(c-a) << endl;
    cout << a % (d*b) << endl;

    // Operaciones vector con numero.
    cout << b+3 << endl;
    cout << a*3.0 + &b << endl;
    cout << (b+b) * (c%a) << endl;
    cout << &(a-3) << endl;
    cout << e-(100+10) << endl;
    cout << &e << endl;
    
    return 0;
}
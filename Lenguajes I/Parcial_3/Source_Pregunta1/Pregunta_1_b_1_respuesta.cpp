/*
    Universidad Simon Bolivar
    Departamento de Computación y Tecnología de la Información
    CI3641 – Lenguajes de Programación 1
    Trimestre: Septiembre - Diciembre 2023
    Profesor: Ricardo Monascal
    Estudiante: Junior Miguel Lara Torres
    Carnet: 17-10303

    Parcial 3 - Pregunta 1.b.1

	"Defina un interfaz o clase abstracta Secuencia, que represente una colección ordenada
    de elementos.
    (...)
    Defina dos clases concretas Pila y Cola que sean subtipo de Secuencia.
	(...)"

    Usando la definicion de clases para tipos genericos, es decir usando
    los templetes "template <typename T>" que representa un tipo de dato
    generico en nuestro caso. En este sentido, me diente la herencia de
    clases y el uso de las librerias ya existencias para Cola y Pilas
    de nombre Queue y Stack respectivamente, se definen los subtipos de
    la clase principal Secuencial de tal forma que se redefinen los
    los metodos de agregar y remover para que sean compatibles segun
    sea Pila o Cola.
*/

#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

// Definicion de clase principal Secuencia que representa una 
// coleccion ordenada de elementos de tipo generico T. Modulada
// por un vector de elementos de tipo T. Este define 3 metodos
// agregar, remover y vacio.
template <typename T>
class Secuencia {
private:
    vector<T> elementos;

public:
    void agregar(T elemento) {
        elementos.push_back(elemento);
    }

    T remover() {
        if (elementos.empty()) {
            throw "Secuencia vacía.";
        }

        T elemento = elementos.back();
        elementos.pop_back();
        return elemento;
    }

    bool vacio() {
        return elementos.empty();
    }
};

// Definicion de clase Pila que representa una pila de 
// elementos de tipo generico T. Modulada por una pila de
// de la libreria proporcionada por C++(Stack). Este 
// redefine los metodos originales de la clase Secuencia 
// incorporando los metodos de la libreria Stack.
template <typename T>
class Pila : public Secuencia<T> {
private:
    stack<T> pila;

public:
    void agregar(T elemento) {
        pila.push(elemento);
    }

    T remover() {
        if (this->vacio()) {
            throw "Pila vacía";
        }
        T elemento = pila.top();
        pila.pop();
        return elemento;
    }

    bool vacio() {
        return pila.empty();
    }
};

// Definicion de clase Cola que representa una cola de 
// elementos de tipo generico T. Simulada por una cola de
// de la libreria proporcionada por C++(Queue). Este 
// redefine los metodos originales de la clase Secuencia 
// incorporando los metodos de la libreria Queue.
template <typename T>
class Cola : public Secuencia<T> {
    private:
    queue<T> cola;

    public:
    void agregar(T elemento) {
        cola.push(elemento);
    }

    T remover() {
        if (this->vacio()) {
            throw "Cola vacía."; 
        }
        T elemento = cola.front();
        cola.pop();
        return elemento;
    }

    bool vacio() {
        return cola.empty();
    }
};

int main() {
    cout << "Pila:\n";
    // Pila de floats
    Pila<float> pilaFloats;
    pilaFloats.agregar(1.5);
    pilaFloats.agregar(2.2); 
    pilaFloats.agregar(3.7);
    cout << endl;
    for(int i = 0; i < 3; i++) cout << "     " << pilaFloats.remover() << endl;

    // Pila de enteros
    Pila<int> pilaEnteros;
    pilaEnteros.agregar(10);
    pilaEnteros.agregar(20);
    pilaEnteros.agregar(30);
    cout << endl;
    for(int i = 0; i < 3; i++) cout << "     " << pilaEnteros.remover() << endl;

    // Pila de strings
    Pila<string> pilaStrings;
    pilaStrings.agregar("hola");
    pilaStrings.agregar("prosol");
    pilaStrings.agregar("!");  
    cout << endl;
    for(int i = 0; i < 3; i++) cout << "     " << pilaStrings.remover() << endl;

    cout << "\nCola:\n";
    // Cola de floats
    Cola<float> colaFloats;
    colaFloats.agregar(1.5);
    colaFloats.agregar(2.2); 
    colaFloats.agregar(3.7);
    cout << endl;
    for(int i = 0; i < 3; i++) cout << "     " << colaFloats.remover() << endl;

    // Cola de enteros
    Cola<int> colaEnteros;
    colaEnteros.agregar(10);
    colaEnteros.agregar(20);
    colaEnteros.agregar(30);
    cout << endl;
    for(int i = 0; i < 3; i++) cout << "     " << colaEnteros.remover() << endl;

    // Cola de strings
    Cola<string> colaStrings;
    colaStrings.agregar("hola");
    colaStrings.agregar("prosol");
    colaStrings.agregar("!");  
    cout << endl;
    for(int i = 0; i < 3; i++) cout << "     " << colaStrings.remover() << endl;
    
    return 0;
}
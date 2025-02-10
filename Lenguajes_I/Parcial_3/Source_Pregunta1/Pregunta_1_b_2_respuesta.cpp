/*
    Universidad Simon Bolivar
    Departamento de Computación y Tecnología de la Información
    CI3641 – Lenguajes de Programación 1
    Trimestre: Septiembre - Diciembre 2023
    Profesor: Ricardo Monascal
    Estudiante: Junior Miguel Lara Torres
    Carnet: 17-10303

    Parcial 3 - Pregunta 1.b.2

	"Defina un tipo de datos que represente grafos como listas de adyacencias 
    y cada nodo sea representado por un número entero (puede usar todas las 
    librerías a su disposición en el lenguaje).
    (...)"

    Mediante el uso de mapas desordenados, colas y pilas ya existentes
    en las librerias de C++, procedemos a implementar dicho tipo de dato
    grafo que simula listas de adyacencias.
*/

#include <iostream>
#include <algorithm>
#include <list>
#include <queue>
#include <stack>
#include <unordered_map>

using namespace std;

// Representación de grafo como lista de adyacencias 
class Grafo {
private:
    unordered_map<int, list<int>> G; 
public:
    void agregarArista(int origen, int destino) {
        if(G.count(origen) == 0) {
            G[origen]; // Inicializa lista vacía
        }
        if(count(G[origen].begin(), G[origen].end(), destino) == 0){
            G[origen].push_back(destino); // Agrega a la lista de adyacencia.
        } else {
            cout << " Arista existente.\n";
        }
    }
    list<int> adyacentes(int nodo) {
        return G[nodo];
    }
    int longitud() {
        return G.size();
    }
    bool no_existe_nodo(int nodo){
        return (G.count(nodo) == 0);
    }
};

// Clase abstracta para búsquedas
class Busqueda {
public:
    int buscar(Grafo g, int D, int H){
        if(g.no_existe_nodo(D)){
            cout << " El nodo origen no existe en el grafo.\n";
            return -1;
        }
        if(D == H) return 1; // Caso directo.

        int cantidad_nodos_explorados = 1; // La raiz misma. 
        list<int> vis; // Lista de visitados.
        vis.push_back(D);
        /*
        **<T> VARIABLE;**
        **VARIABLE.funcion1();**

        while(!VARIABLE.empty()){
            int nodo = **VARIABLE.funcion2();**
            **VARIABLE.funcion3();**
            cantidad_nodos_explorados++;
            list<int> adyacentes_de_nodo = g.adyacentes(nodo);
            for(auto it : adyacentes_de_nodo){                
                if(it == H) return cantidad_nodos_explorados;
                if(count(vis.begin(), vis.end(), it) != 0) continue;
                vis.push_back(it);
                **VARIABLE.funcion1();**
            }
        }
        */
        return -1; // Cado de no encontrar H. 
    }
};

// Clase DFS que simula la busqueda en profundidad mediante el
// uso de pilas.
class DFS : public Busqueda {
public:
    int buscar(Grafo g, int D, int H) {
        if(g.no_existe_nodo(D)){
            cout << " El nodo origen no existe en el grafo.\n";
            return -1;
        }
        if(D == H) return 1; // Caso directo.

        int cantidad_nodos_explorados = 0;
        list<int> vis; // Lista de visitados.
        vis.push_back(D);
        stack<int> pila; // Pila del DFS.
        pila.push(D);

        while(!pila.empty()){
            int nodo = pila.top();
            pila.pop();
            cantidad_nodos_explorados++;
            list<int> adyacentes_de_nodo = g.adyacentes(nodo);
            for(auto it : adyacentes_de_nodo){
                if(it == H) return cantidad_nodos_explorados;
                if(count(vis.begin(), vis.end(), it) != 0) continue;
                vis.push_back(it);
                pila.push(it);
            }
        }
        return -1;
    }
};

// Clase BFS que simula la busqueda en amplitud mediante el
// uso de colas.
class BFS : public Busqueda {
public:
    int buscar(Grafo g, int D, int H) {
        if(g.no_existe_nodo(D)){
            cout << " El nodo origen no existe en el grafo.\n";
            return -1;
        }
        if(D == H) return 1; // Caso directo.

        int cantidad_nodos_explorados = 0; // La raiz misma. 
        list<int> vis; // Lista de visitados.
        vis.push_back(D);
        queue<int> cola; // Cola del BFS.
        cola.push(D);

        while(!cola.empty()){
            int nodo = cola.front();
            cola.pop();
            cantidad_nodos_explorados++;
            list<int> adyacentes_de_nodo = g.adyacentes(nodo);
            for(auto it : adyacentes_de_nodo){
                if(it == H) return cantidad_nodos_explorados;
                if(count(vis.begin(), vis.end(), it) != 0) continue;
                vis.push_back(it);
                cola.push(it);
            }
        }
        return -1;
    }
};

int main() {
/*
                  1
               /     \
             /         \
           /             \    
          2 -------------> 9
        /   \           /     \
      3 <--- 6         10      13
     /  \   /  \     /  \      /  \
    4--->5 7    8->11-->12-->14   15
*/
    Grafo g;
    g.agregarArista(1, 2);
    g.agregarArista(1, 9);
    g.agregarArista(2, 9);
    g.agregarArista(2, 3);
    g.agregarArista(3, 4);
    g.agregarArista(3, 5);
    g.agregarArista(4, 5);
    g.agregarArista(6, 2);
    g.agregarArista(6, 3);
    g.agregarArista(6, 7);
    g.agregarArista(6, 8);
    g.agregarArista(8, 11);
    g.agregarArista(9, 10);
    g.agregarArista(10, 11);
    g.agregarArista(11, 12);
    g.agregarArista(12, 10);
    g.agregarArista(12, 14);
    g.agregarArista(13, 9);
    g.agregarArista(14, 13);
    g.agregarArista(15, 13);
    
    int D;
    int H;
    cout << "\n* ~/ >> Indique nodo origen D: "; cin >> D;
    cout << "* ~/ >> Indique nodo destino H: "; cin >> H;

    DFS dfs;
    int explorados_dfs = dfs.buscar(g, D, H);

    BFS bfs;
    int explorados_bfs = bfs.buscar(g, D, H);

    if(explorados_dfs == -1 || explorados_bfs == -1 ) {
        cout << "\n* ~/ >> ** No existe camino entre D y H. **\n\n";
    } else { 
        printf("\n* ~/ >> Desde %d a %d con DFS: %d nodos explorados.\n", D, H, explorados_dfs);
        printf("\n* ~/ >> Desde %d a %d con BFS: %d nodos explorados.\n\n", D, H, explorados_bfs);
    }

    return 0;
}

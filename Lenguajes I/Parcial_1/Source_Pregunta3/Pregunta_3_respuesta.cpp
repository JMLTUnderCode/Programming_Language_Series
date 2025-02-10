/*
    Universidad Simon Bolivar
    Departamento de Computación y Tecnología de la Información
    CI3641 – Lenguajes de Programación 1
    Trimestre: Septiembre - Diciembre 2023
    Profesor: Ricardo Monascal
    Estudiante: Junior Miguel Lara Torres
    Carnet: 17-10303

    Parcial 1 - Pregunta 3

	"Se desea que modele e implemente, en el lenguaje de su elección, un programa que simule
	un manejador de memoria que implementa el buddy system. Este programa debe cumplir
	con las siguientes características:
	Al ser invocado, recibirá como argumento la cantidad de bloques de memoria que
	manejará.
	..."

	g++ -c Pregunta_3_respuesta.cpp
	g++ -o (nombre) Pregunta_3_respuesta.o
	./(nombre) (capacidad de memoria)

	Si se quiere ver la cobertura se debe instalar gcovr y luego
    aplicas los siguientes comandos:

    g++ --coverage -c Pregunta_3_respuesta.cpp
    g++ --coverage -o (nombre) Pregunta_3_respuesta.o
    ./(nombre) (capacidad de memoria)
	  *aplique todos los comandos descritos en el PDF respuesta*
    gcovr
*/

#include <iostream>
#include <math.h>
#include <list>
#include <cstring>
#include <sstream>

// Directivas FOR
#define FOR(i, x, n) for(int i = x; i-x < n; i++)

using namespace std;

// Variables de entorno global.
list<string> INDENTIFIERS; 	// Identificador de cada reserva de memoria.
int N; 						// Numero de bloques totales.

// Definicion de clase memory, simula la lista principal doblemente enlazada.
struct Memory{
	// Definicion de clase MemoryNode, simula el nodo de la lista de memoria.
	struct MemoryNode{
		int blocks;				 // Numero de bloques en el nodo de la memoria.
		string indentifier;		 // Identificador.
		struct MemoryNode *prev; // Apuntador al anterior.
		struct MemoryNode *next; // Apuntador al siguiente.
		
		// Constructor de clase interna.
		MemoryNode(int _b){ 
			blocks = _b; indentifier = "";
			prev = NULL; next = NULL;
		}
	};

	struct MemoryNode *head;

	// Constructor de clase externa.
	Memory(int capacity){
		head = new struct MemoryNode(capacity);
	}
	
	// Precedimiento que permite reservar un segmento de memoria dado el numero
	// de bloques y el identificador. Se verifica si existe espacio y no repeticion
	// del identificador.
	void reserve(int new_blocks, string new_iden){
		// Verificamos que el identificador nuevo sea unico.
		bool status;
		for(auto it : INDENTIFIERS){
			status = strcmp(new_iden.c_str(), it.c_str()) == 0;
			if(status) {
				cout << "     **-> ERROR 406 <-**\n          Este nombre ya tiene reservado memoria en el sistema. \n";
				return;
			}
		}
		
		// Realizamos la busqueda de un segmento libre que contenga almenos los necesarios
		// para satisfacer la solicitud del usuario.
		MemoryNode *current = head;
		while(current != NULL){
			// Verificado que el estado del segmento sea libre.
			status = strcmp(current->indentifier.c_str(), "") == 0;

			// Si el espacio esta libre y la cantidad de bloques es suficiente entonces
			// creamos dos nuevo nodos en (y -> reservado -> libre restante -> x) donde 
			// x e y son otros nodos cualquiera quiera sea NULL reservado.
			if (status && new_blocks <= current->blocks){
				INDENTIFIERS.push_back(new_iden);
				current->indentifier = new_iden;
				if(current->blocks - new_blocks > 0){
					MemoryNode *temp = new struct MemoryNode(0);
					temp->blocks = current->blocks - new_blocks;
					current->blocks = new_blocks;
					temp->prev = current;
					temp->next = current->next;
					current->next = temp;					
				}
				break;
			
			// En caso de no encontrar un segmento que satisfaga la solicitud entonces
			// retornamos un mensaje de error.
			} else if (current->next == NULL) {
				cout << "     **-> ERROR 404 <-**\n          No existe memoria suficiente para satisfacer la solicitud.\n";
				break;
			
			// Iterando por los nodos de la memoria
			} else {
				current = current->next;
			}
		}
	}

	// Procedimiento que permite liberar memoria dado del identificador del bloque
	// anteriormente reservado.
	void free(string new_iden){
		// Verificamos que el identificador nuevo sea unico.
		bool status;
		MemoryNode *current = *&head;
		while(current != NULL){
			status = strcmp(current->indentifier.c_str(), new_iden.c_str()) == 0;
			if(status){
				INDENTIFIERS.remove(current->indentifier); // Borramos identificador.
				current->indentifier = ""; // Pasamos a estado libre.
				bool status_right, status_left;
				if(current->prev == NULL || current->next == NULL){ // Caso extremos de la memoria.
					if(current->prev == NULL){
						status_right = strcmp(current->next->indentifier.c_str(), "") == 0; // Estado del segmento a la derecha.
						status_left = false; // Estado izquierda falso dado al NULL.
					} else {
						status_left = strcmp(current->prev->indentifier.c_str(), "") == 0; // Estado del segmento a la izquierda.	
						status_right = false; // Estado derecha falso dado al NULL.
					}
					
				} else { // Caso interno/centro de la memoria.
					status_right = strcmp(current->next->indentifier.c_str(), "") == 0; // Estado del segmento a la derecha.
					status_left = strcmp(current->prev->indentifier.c_str(), "") == 0; // Estado del segmento a la izquierda.
				}
				
				// Reagrupamos los bloques libres, compactando dos a tres bloques libres contiguos
				// en uno solo bloque y la modificacion de los apuntadores respectivos.
				MemoryNode *temp;
				if(status_left && status_right){ // Ambos segmentos libres
				
					current = current->prev;
					current->blocks += current->next->blocks + current->next->next->blocks;
					temp = current->next->next->next;
					delete current->next->next;
					
				} else if (status_left){ // Solo segmento izquierdo libre.
					current = current->prev;
					current->blocks += current->next->blocks;
					temp = current->next->next;

				} else if (status_right){ // Solo ssgmento derecho libre.
					current->blocks += current->next->blocks;
					temp = current->next->next;
				}

				// En caso de haber realizado algun cambio en los apuntadores.
				// Realizamos las posteriores aplicaciones de la lista doblemente
				// enlazada.
				if(status_right || status_left){
					delete current->next;
					current->next = temp;
					if(temp != NULL) {temp->prev = current;}
				}
				return;

			} else {
				current = current->next;
			}
		}
		cout << "     **-> ERROR 405 <-**\n          No existe asignacion de memoria asociado a ese nombre.\n";
	}
	
	// Procedimiento que permite mostrar por pantalla la cantidad de bloques en potencias
	// de dos disponibles en la memoria actual.
	void show(){
		// Inicializacion de variables.
		int list_free[N+1] = {0}; // Arreglo de potencias de dos que contiene la memoria.
		int m, p, count, actual_pow, free_m;
		
		// Iteramos por la lista doublemente enlazada.
		MemoryNode *current = head;
		while(current != NULL){
			// Verificando que el segmento este libre y en caso afirmativo determinar
			// los segmentos en potencia de 2 libres.
			if(strcmp(current->indentifier.c_str(), "") == 0){
				count = 0;
				while(current->blocks - count > 0){
					m = floor(log2(current->blocks - count));
					actual_pow = pow(2,m);
			    	count += actual_pow;
			    	list_free[actual_pow]++;
				}
			}
			current = current->next;
		}
		
		// Mostramos lista de bloques disponibles.
		cout << "     ** Lista de segmentos de bloques libres: \n";
		FOR(x, 0, (int)floor(log2(N))+1){
			p = pow(2,x);
			cout << "        |" << p << "| -> " << list_free[p] << endl;
		}

		// Mostramos la lista de nombres reservados con sus respectivos bloques.
		current = head; free_m = 0;
		cout << "\n     ** Lista de nombres reservados:\n";
		while(current != NULL){
			if(strcmp(current->indentifier.c_str(), "") != 0){
				cout << "        -- " << current->indentifier << ": " << current->blocks << " bloques.\n";
			} else {
				free_m += current->blocks;
			}
			current = current->next;
		}

		// Mostramos total de bloques disponibles.
		cout << "\n     ** Numero disponible de bloques totales:\n        -- " << free_m << "\n\n";
	}
};

// Funcion que permite pasar un string a su version UPPERCASE.
string toUpper(string str) {
  FOR(c, 0, str.length()) {str[c] = toupper(str[c]); } 
  return str;
}

// Manipulacion de entrada-salida de datos, corroboracion de inputs,
// aplicaciones de metodos para retornos de respuesta segun sea el caso.
int main(int argc, char const *argv[]) {
    if(argc > 1 && argc < 3){
        N = atoi(argv[1]); // Numero total de bloques de memoria.
  		Memory main_memory(N); // Memoria principal con N bloques.
  		
		cout << "----------------------------------------------------\n";
		cout << "----------Console: Buddy System Simulation----------\n";
  		string word, name;
  		const char *command_cov;
  		int n_block;
  		
		// Rutina que permite solicitar comandos constantemente y realizar procedimientos.
  		while(true){
  			cout << "~/ >> ";
  			list<string> parameters;
  			char command[80];
  			
			// Lectura de comando
			cin.getline(command, 80, '\n');
  			
			// Desglozado de comando.
  			stringstream input_stringstream(command);  
  			while(getline(input_stringstream, word, ' ')){
  				parameters.push_back(word);
			}

			// Verificacion de parametros.
			if(parameters.size() < 1 || parameters.size() > 3){
				cout << "     **-> ERROR 401: Faltan o excede el numero de argumentos permitidos.\n";
				continue;
			}

			// Buscar la coincidencia del comando dado por con comandos permitidos.
  			list<string>::iterator it = parameters.begin();
  			command_cov = toUpper(*it).c_str();
  			
  			if(strcmp("RESERVAR", command_cov) == 0){
  				it++; n_block = atoi(it->c_str());
				if(n_block == 0){
					cout << "     **-> ERROR 402 <-**\n          Sintaxis erronea. Ingrese HELP para mostrar los comandos disponibles.\n";
					continue;
				}
  				it++; name = *it;
  				main_memory.reserve(n_block, name);
  				
			} else if (strcmp("LIBERAR", command_cov) == 0){
				it++; name = *it;
				main_memory.free(name);	
				
			} else if (strcmp("MOSTRAR", command_cov) == 0){
				main_memory.show();
				
			} else if (strcmp("SALIR", command_cov) == 0){
				break;
				
			} else if (strcmp("HELP", command_cov) == 0){
				cout << "     Lista de comandos para Buddy System Simulation:\n";
				cout << "          - RESERVAR <capacidad(int)> <nombre(string)> \n";
				cout << "          - LIBERAR <nombre(string)> \n";
				cout << "          - MOSTRAR  \n";
				cout << "          - SALIR  \n";
				cout << "     Se permiten sus respectivas versiones en minusculas.\n";
				
  			} else {
  				cout << "     **-> ERROR 403 <-**\n          Comando invalido. Ingrese HELP para mostrar los comandos disponibles.\n";
			}
		}
    } else {
        cout << "     **-> FATAL ERROR <-**\n          Error: Numero de argumentos incorrectos." << endl;
    }
    
    return 0;
}
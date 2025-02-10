#   (VERSION NO FUNCIONAL)

import re

def extraer_datos(cadena):

  nombre = cadena.split('(')[0]

  hechos = []
  variables = {}

  if '(' in cadena:  
    params = cadena.split('(')[1].rstrip(')')
    print(params)
    pila = []
    hecho_actual = []

    for i,c in enumerate(params):
      if c == '(':
        pila.append(i)
      elif c == ')':
        inicio = pila.pop()
        hecho = ''.join(hecho_actual)
        hechos.append(hecho)
        variables[hecho] = []
        hecho_actual = []
      elif c.isupper():
        hecho_actual.append(c)
        variables[hecho].append(c)
      else:
        hecho_actual.append(c)

  return nombre, hechos, variables

class Prolog():
    def __init__(self) -> None:

        self.DATA_FACTS = []

        # Diccionario de reglas, la llave es el consecuente y el atributo es un lista
        # de antecedentes.
        self.DATA_RULES = {}

        self.DATA_ARGS = {}

        # Informacion de errores.
        self.ERROR_DEF = ""
        self.ERROR_ASK = ""

    def DEF(self, data):
        # Veridicar si alguno de los predicados es true o false. como palabra reservada.
        "DEF in(c(e,P), aca(t(i, o(N)))) ayer(N, P)"
        "DEF true"
        
        # Para el caso de tener un hecho.
        if ( len(data) == 1):
            fact = data[0]

        # Para el caso de tener una regla.
        else:
            consequent = data[0]
            antecedents = data[1:]

        entrada = "in(c(Xer, P), aca(t(i, o(N))))"
        print([1,2,3,4])
        print(extraer_datos(entrada))            

        # Verificamos la creacion del predicado.
        creation_check = confirming_definition(data)
        print(f"* ~/ >> - Success \'" + creation_check + ("\'"+ " "*(58 - len(creation_check))) + "*")

    def ASK(self, data):
        pass


def confirming_definition(data):
    creation_check = f"{data[0]}"
    for i in range(len(data)):
        print(data[i])

    if len(data) == 2:
        creation_check += f" :- {data[1]}."
    elif len(data) > 2:
        creation_check += f" :- {data[1]}, "
        for i in range(2, len(data)):
            creation_check += data[i]
            if i < len(data)-1:
                creation_check += ', '
        creation_check += '.'
    return creation_check
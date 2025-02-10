import math

BYTES_BLOCK = 4 # Numero de bytes para cada bloque de la pila.

# Clase principal de manejador de datos.
class DataDrive():
    def __init__(self) -> None:
        # Diccionarios principales de cada dato.
        self.DATA_ATOMIC = {}
        self.DATA_STRUCT = {}
        self.DATA_UNION  = {}

        # Tipos de datos
        self.TYPES_ATOMIC = {}
        self.TYPES_STRUCT = {}
        self.TYPES_UNION  = {}

        # Informacion de errores.
        self.ERROR_ATOMIC = ""
        self.ERROR_STRUCT = ""
        self.ERROR_UNION  = ""
        self.ERROR_DESCRIBIR = ""

    def ATOMIC(self, data):
        # Extraccion de datos.
        name_type = data[0]
        self.ERROR_ATOMIC = ""
        
        if data[1].isdigit() and data[2].isdigit():
            representation = int(data[1])
            alignment = int(data[2])
            # Verificacion de existencia y actualizacion de error o data.
            if all(list(map((lambda x: name_type not in x.keys()), [self.DATA_ATOMIC, self.DATA_STRUCT, self.DATA_UNION]))):
                self.DATA_ATOMIC[name_type] = [representation, alignment]

            # Si el nombre del ATOMIC ya existe se reporta el error.
            else:
                self.ERROR_ATOMIC = f"{name_type} is already defined"

        # Si la aliniacion o la representacion son incorrectas.
        else :
            self.ERROR_ATOMIC = "Just numbers for representation and alignment"
  
    def STRUCT(self, data):
        # Extraccion de datos.
        name_type = data[0]
        types = data[1:]
        self.ERROR_STRUCT = ""

        # Estado de verificacion de los subtipos que definen a la STRUCT.
        status = True

        # Verificacion de existencias para el nombre del tipo de dato.
        if all(list(map((lambda x: name_type not in x.keys()), [self.DATA_ATOMIC, self.DATA_STRUCT, self.DATA_UNION]))):
            
            # Verificacion de que cada tipo que define al nombre anterior este definido al menos una vez.
            for type in types:
                if any(list(map((lambda x: type in x.keys()), [self.DATA_ATOMIC, self.DATA_STRUCT, self.DATA_UNION]))):            
                    continue
                else:
                    self.ERROR_STRUCT = f"{type} is not defined"
                    status = False
                    break

            # Si todos los tipos que definen a la STRUCT estan definidos.
            if status:
                self.DATA_STRUCT[name_type] = types

        # Si el nombre de la STRUCT ya existe se reporta el error.
        else:
            self.ERROR_STRUCT = f"{name_type} is already defined"

    def UNION(self, data):
        # Extraccion de datos.
        name_type = data[0]
        types = data[1:]
        self.ERROR_UNION = ""

        # Estado de verificacion de los subtipos que definen a la UNION.
        status = True

        # Verificacion de existencias para el nombre del tipo de dato.
        if all(list(map((lambda x: name_type not in x.keys()), [self.DATA_ATOMIC, self.DATA_STRUCT, self.DATA_UNION]))):
            
            # Verificacion de que cada tipo que define al nombre anterior este definido al menos una vez.
            for type in types:
                if any(list(map((lambda x: type in x.keys()), [self.DATA_ATOMIC, self.DATA_STRUCT, self.DATA_UNION]))):            
                    pass
                else:
                    self.ERROR_UNION = f"{type} is not defined"
                    status = False
                    break

            # Si todos los tipos que definen a la UNION estan definidos.
            if status:
                self.DATA_UNION[name_type] = types
        
        # Si el nombre de la UNION ya existe se reporta el error.
        else:
            self.ERROR_UNION = f"{name_type} is already defined"

    # Funcon que realiza el calculo de la memoria total, aliniamientos y memoria perdida.
    def DESCRIPTING(self, name_data, mode, description, stack):
        if mode == 0: # MODO SIN EMPAQUETAR
            if name_data in self.DATA_ATOMIC.keys():
                memory_type = self.DATA_ATOMIC[name_data][0]
                memory_used = math.ceil(memory_type/BYTES_BLOCK)*BYTES_BLOCK

                alignment_type = self.DATA_ATOMIC[name_data][1]
                actual_size_stack = len(stack)
                iter_stack = 0
                step = math.ceil(alignment_type/BYTES_BLOCK)

                # Buscamos la direccion correspondiente al aliniamiento del dato.
                while True:

                    # Nivelacion de memoria relativo al iterador del stack.
                    if stack[iter_stack] != 4:
                        iter_stack += step
                        for x in range(0, iter_stack - actual_size_stack + step):
                            stack.append(4)
                    
                    # Encontramos una direccion de memoria libre y lista para ser usada.
                    else:
                        # Verificar si hay memoria suficiente                        
                        aux = iter_stack
                        for x in range(0, step-1):
                            aux += 1
                            if aux < actual_size_stack:
                                if stack[aux] != 4:
                                    iter_stack += step
                                    continue

                        # Agregamos bloques a la pila sino tenemos suficiente memoria 
                        # relativa al iterador del stack.
                        for x in range(0, iter_stack - actual_size_stack + step):
                            stack.append(4)

                        # Empezamos a llenar la pila.
                        aux = 0
                        for x in range(0, step):
                            if aux + 4 < memory_type:
                                stack[iter_stack] = 0
                            else:
                                stack[iter_stack] = 4 - (memory_type - aux)
                            aux += 4
                            iter_stack += 1
                        break                       

            elif name_data in self.DATA_STRUCT.keys():
                internal_stack = [4]
                
                # Iteramos por cada tipo definido para la STRUCT.
                for type in self.DATA_STRUCT[name_data]:
                    (internal_description, internal_stack) = self.DESCRIPTING(type, 0, [0, 0, 0], internal_stack)                    

                # Actualizacion de la descripcion para la STRUCT sobre la memoria, aliniacion y desperdicio.
                memory_used = len(internal_stack)*4
                description[0] += memory_used - internal_stack[-1]         # Sumamos memoria usada de la STRUCT en la pila.
                description[1] += memory_used                              # Sumamos alinicion directa de la STRUCT en la pila.
                description[2] += sum(internal_stack) - internal_stack[-1] # Memoria perdida = Usada menos memoria del tipo.
                stack += internal_stack

            elif name_data in self.DATA_UNION.keys():
                internal_stack = [4]
                
                # Iteramos por cada tipo definido para la STRUCT.
                for type in self.DATA_UNION[name_data]:
                    (internal_description, internal_stack) = self.DESCRIPTING(type, 0, [0, 0, 0], internal_stack)                    

                # Actualizacion de la descripcion para la UNION sobre la memoria, aliniacion y desperdicio.
                memory_used = len(internal_stack)*4
                description[0] += memory_used - internal_stack[-1]         # Sumamos memoria usada de la STRUCT en la pila.
                description[1] += memory_used                              # Sumamos alinicion directa de la STRUCT en la pila.
                description[2] += sum(internal_stack) - internal_stack[-1] # Memoria perdida = Usada menos memoria del tipo.
                stack += internal_stack

        elif mode == 1: # MODO EMPAQUETADO
            if name_data in self.DATA_ATOMIC.keys():
                description[0] += self.DATA_ATOMIC[name_data][0] # Sumamos memoria usada directamente.

            elif name_data in self.DATA_STRUCT.keys():
                for type in self.DATA_STRUCT[name_data]:
                    (description, stack) = self.DESCRIPTING(type, 1, description, [])
                    description[1] = math.ceil(description[0]/4)*4 # Determinamos aliniacion segun la memoria total.

            elif name_data in self.DATA_UNION.keys():
                for type in self.DATA_UNION[name_data]:
                    (description, stack) = self.DESCRIPTING(type, 1, description, [])
                    description[1] = math.ceil(description[0]/4)*4 # Determinamos aliniacion segun la memoria total.

        elif mode == 2: # MODO OPTIMIZADO
            if name_data in self.DATA_ATOMIC.keys():
                pass

            elif name_data in self.DATA_STRUCT.keys():
                pass

            elif name_data in self.DATA_UNION.keys():
                pass
        
        return (description, stack)

    def DESCRIBIR(self, name_data):
        self.ERROR_DESCRIBIR = ""
        if any(list(map((lambda x: name_data in x.keys()), [self.DATA_ATOMIC, self.DATA_STRUCT, self.DATA_UNION]))):
            (unpacked, stack_unpacked)   = self.DESCRIPTING(name_data, 0, [0, 0, 0], [4])
            (packed, stack_packed)       = self.DESCRIPTING(name_data, 1, [0, 0, 0], [4])
            (optimized, stack_optimized) = self.DESCRIPTING(name_data, 2, [0, 0, 0], [4])
            return [unpacked, packed, optimized]

        else:
            self.ERROR_STRUCT = f"{name_data} is not defined"
            return [-1,-1,-1]


    
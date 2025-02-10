# Definicion de la clase VirtualTable que simula la tabla de metodos virtuales,
# esta define dos metodos importantes CLASE y DESCRIBIR, por un lado CLASE se
# encarga de agregar incorporar a la lista de clases definidas, y por otro lado
# DESCRIBIR se encarga de reporta la lista de metodos respectivo para la clasa
# pedida.
class VirtualTable():
    def __init__(self) -> None:
        # Lista de clases definidas.
        self.DATA_CLASS = []

        # Diccionario de metodos de cada clase.
        self.METHOD_CLASS = {}

        # Informacion de errores.
        self.ERROR_CLASS = ""
        self.ERROR_DESCRIBIR = ""

    def CLASE(self, data):
        # Extraccion de datos.
        name_class = ""
        name_subclass = ""
        methods = []
        if len(data) > 1:
            if(data[1] == ':'):
                name_subclass = data[0]
                name_class = data[2]
                if(len(data) > 3):
                    methods = data[3:]
            else:
                name_class = data[0]
                methods = data[1:]
        else:
            name_class = data[0]

        self.ERROR_CLASS = ""

        # Verificamos que no se repitan definiciones de metodos.
        for i in range(0, len(methods)):
            if methods.count(methods[i]) > 1:
                self.ERROR_CLASS = f" Method {methods[i]} is already defined."
                return

        # No existe subclase.
        if name_subclass == "":
            # Verificamos que la nueva clase no existe.
            if name_class not in self.DATA_CLASS:
                # Se define la nueva clase.
                self.DATA_CLASS.append(name_class)
                self.METHOD_CLASS[name_class] = []
                for i in range(0, len(methods)):
                    self.METHOD_CLASS[name_class].append([methods[i], name_class])

            # Error de existencia de clase en caso contrario.
            else:
                self.ERROR_CLASS = f" Class {name_class} is already defined."    

        # Existe subclase.
        elif name_subclass not in self.DATA_CLASS: 
            # Verificamos que la clase padre exista.
            if name_class in self.DATA_CLASS:
                self.DATA_CLASS.append(name_subclass)
                self.METHOD_CLASS[name_subclass] = []

                # Agregamos los metodos respectivo de la subclase.
                for i in range(0, len(methods)):
                    self.METHOD_CLASS[name_subclass].append([methods[i], name_subclass])

                # Agregamos los metodos heredados de la clase padre.
                methods_super_class = self.METHOD_CLASS[name_class]
                for i in range(0, len(methods_super_class)):
                    # Verificamos que el metodo no exista en la subclase.
                    if methods_super_class[i][0] not in methods:
                        self.METHOD_CLASS[name_subclass].append(methods_super_class[i])
            
            # Error de inexistencia de clase en caso contrario.
            else:
                self.ERROR_CLASS = f" Class {name_class} is not defined."

        # Error de subclase ya esta definida.
        else:
            self.ERROR_CLASS = f" Class {name_subclass} is already defined."  

    def DESCRIBIR(self, name):
        # Verificamos que la clase exista.
        self.ERROR_DESCRIBIR = ""
        if name in self.DATA_CLASS:
            return self.METHOD_CLASS[name]
        else:
            self.ERROR_DESCRIBIR = f" Class {name} is not defined."

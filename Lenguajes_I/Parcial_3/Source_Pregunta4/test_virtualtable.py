from virtualtable import *

####################################################################
### Prueba para la clase VirtualTable

def test_VirtualTable_CLASE_SIN_METODOS():
    table = VirtualTable()
    table.CLASE(["A"])
    assert ( table.DATA_CLASS == ["A"] )

def test_VirtualTable_CLASE_CON_METODOS():
    table = VirtualTable()
    table.CLASE(["A", "f", "g"])
    assert ( table.METHOD_CLASS["A"] == [["f","A"], ["g","A"]] )

def test_VirtualTable_DESCRIBIR():
    table = VirtualTable()
    table.CLASE(["A", "f", "g"])
    table.CLASE(["B", ":", "A", "h", "i", "f"])
    desc = table.DESCRIBIR("B")
    assert ( desc == [["h","B"], ["i","B"], ["f","B"], ["g", "A"]] )

def test_VirtualTable_DESCRIBIR_CLASE_SIN_METODO():
    table = VirtualTable()
    table.CLASE(["A"])
    desc = table.DESCRIBIR("A")
    assert ( desc == [] )

def test_VirtualTable_ERROR_REPITE_CLASE():
    table = VirtualTable()
    table.CLASE(["A", "f", "g"])
    table.CLASE(["B", ":", "A", "h", "i", "f"])
    table.CLASE(["B", ":", "C", "a", "b"])
    assert ( table.ERROR_CLASS == " Class B is already defined." )

def test_VirtualTable_ERROR_REPITE_METODO():
    table = VirtualTable()
    table.CLASE(["A", "f", "f"])
    assert ( table.ERROR_CLASS == " Method f is already defined." )
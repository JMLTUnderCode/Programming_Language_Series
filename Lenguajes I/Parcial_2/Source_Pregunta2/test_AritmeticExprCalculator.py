from AritmeticExprCalculator import *

####################################################################
### Prueba para la clase Operacion

# Para la funcion EVAL en version PRE
def test_AritmeticExprCalculator_Operation_EVAL_PRE ():
    expr = Operation("+ + * + 3 4 5 5 / 4 + 1 1")
    expr.EVAL("PRE")
    assert ( expr.stack_eval[0] == 42 )

def test_AritmeticExprCalculator_Operation_EVAL_PRE_Error ():
    expr = Operation("+ + * + 3 4 5 5 / 4 1 + 1")
    assert ( expr.EVAL("PRE") == False)

# Para la funcion EVAL en version POST
def test_AritmeticExprCalculator_Operation_EVAL_POST ():
    expr = Operation("16 1 1 + / 3 - 8 4 4 + * +")
    expr.EVAL("POST")
    assert ( expr.stack_eval[0] == 69 )

def test_AritmeticExprCalculator_Operation_EVAL_POST_Error ():
    expr = Operation("+ + * + 3 4 5 5 / 4 2")
    assert ( expr.EVAL("POST") == False)

#Prueba para la funcion MOSTRAR en version PRE
def test_AritmeticExprCalculator_Operation_MOSTRAR_PRE ():
    expr = Operation("+ + * + 3 4 5 5 / 4 + 1 1")
    expr.MOSTRAR("PRE")
    assert ( expr.stack_mostrar[0] == "(3 + 4) * 5 + 5 + 4 / (1 + 1)" )

def test_AritmeticExprCalculator_Operation_MOSTRAR_PRE_Error ():
    expr = Operation("+ + * + 3 4 5 5 4 2 /")
    assert ( expr.MOSTRAR("PRE") == False)

# Prueba para la funcion MOSTRAR en version PRE
def test_AritmeticExprCalculator_Operation_MOSTRAR_POST ():
    expr = Operation("16 1 1 + / 3 - 8 4 4 + * +")
    expr.MOSTRAR("POST")
    assert ( expr.stack_mostrar[0] == "16 / (1 + 1) - 3 + 8 * (4 + 4)" )

def test_AritmeticExprCalculator_Operation_MOSTRAR_POST_Error ():
    expr = Operation("- 16 1 1 + / 3 8 4 4 + * +")
    assert ( expr.MOSTRAR("POST") == False )

####################################################################
### Prueba para las funciones de verificacion de expresiones.

# Para is_Not_Symbol_Expression
def test_AritmeticExprCalculator_is_Not_Symbol_Expression_1 ():
    assert(is_Not_Symbol_Expression('+') == False)

def test_AritmeticExprCalculator_is_Not_Symbol_Expression_2 ():
    assert(is_Not_Symbol_Expression('M') == True)

# Para is_Not_Evaluation_Order
def test_AritmeticExprCalculator_is_Not_Evaluation_Order_1 ():
    assert(is_Not_Evaluation_Order("PRE") == False)

def test_AritmeticExprCalculator_is_Not_Evaluation_Order_2 ():
    assert(is_Not_Evaluation_Order("POST") == False)

def test_AritmeticExprCalculator_is_Not_Evaluation_Order_3 ():
    assert(is_Not_Evaluation_Order("ANYWARE") == True)

# Para is_Not_Correct_Expression
def test_AritmeticExprCalculator_is_Not_Correct_Expression_2 ():
    assert(is_Not_Correct_Expression("16 1 1 + / 3 - 8 4 4 + * +") == False)

def test_AritmeticExprCalculator_is_Not_Correct_Expression_1 ():
    assert(is_Not_Correct_Expression("16 1 1 + / 3 - 8 4 4 + * + +") == True)

def test_AritmeticExprCalculator_is_Not_Correct_Expression_3 ():
    assert(is_Not_Correct_Expression("16 1 -1 + / 3 - 8 4 4 + * +") == True)

def test_AritmeticExprCalculator_is_Not_Correct_Expression_4 ():
    assert(is_Not_Correct_Expression("16 1 1 % / 3 - 8 4 4 + * +") == True)
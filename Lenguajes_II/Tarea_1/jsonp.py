import re
import string

from parsec import *

# Espacio en blanco
whitespace = regex(r'\s*', re.MULTILINE)

lexeme = lambda p: p << whitespace

# Lista de Tokens
numbers = lexeme(regex(r'-?(0|[1-9][0-9]*)([.][0-9]+)?([eE][+-]?[0-9]+)?').parsecmap(float))
lbrace = lexeme(string('{'))
rbrace = lexeme(string('}'))
lbrack = lexeme(string('['))
rbrack = lexeme(string(']'))
colon = lexeme(string(':'))
comma = lexeme(string(','))
true = lexeme(string('true')).result(True)
false = lexeme(string('false')).result(False)
null = lexeme(string('null')).result(None)

def characterSequence():
    '''Parsear una secuencia de caracteres. (Una secuencia normal incluido caracteres con escape)'''
    def characterSequence_normal():
        '''Caso de secuencia de caracteres normal.'''
        return regex(r'[^"\\]+')

    def characterSequence_escape():
        '''Caso de secuencia de caracteres con escape.'''
        return string('\\') >> (
            string('\\')
            | string('/')
            | string('"')
            | string('b').result('\b')
            | string('f').result('\f')
            | string('n').result('\n')
            | string('r').result('\r')
            | string('t').result('\t')
            | regex(r'u[0-9a-fA-F]{4}').parsecmap(lambda s: chr(int(s[1:], 16)))
        )
    return characterSequence_normal() | characterSequence_escape()

@lexeme
@generate
def strings():
    '''Parsear cadenas de caracteres.'''
    yield string('"')
    body = yield many(characterSequence())
    yield string('"')
    return ''.join(body)

@generate
def Y():
    '''Produccion: Y -> ,VY | lambda'''
    yield comma
    v = yield value
    r = [v]
    y = yield optional(Y, None)
    
    if y:
        r += y
    return r

@generate
def X():
    '''Produccion: X -> VY'''
    v = yield value
    r = [v]
    y = yield optional(Y, None)
    
    if y:
        r += y
    return r

@generate
def array():
    '''Parsear un arreglo de elementos. Produccion: J -> [X]'''
    yield lbrack
    elements = yield optional(X, None)
    yield rbrack
    if elements is None:
        return []
    return elements

@generate
def R():
    '''Produccion: R -> ,s:VR | lambda'''
    yield comma
    key = yield strings
    yield colon
    val = yield value
    
    rest = yield optional(R, None)
    if rest:
        return [(key, val)] + rest
    return [(key, val)]

@generate
def L():
    '''Produccion: L -> s:VR'''
    key = yield strings
    yield colon
    val = yield value
    
    rest = yield optional(R, None)
    if rest:
        return [(key, val)] + rest
    return [(key, val)]

@generate
def object():
    '''Parsear objeto JSON. Produccion: J -> {L}'''
    yield lbrace
    pairs = yield optional(L, None)
    yield rbrace
    if pairs is None:
        return {}
    return dict(pairs)

J = object | array

value = strings | numbers | true | false | null | J
    
jsonp = whitespace >> J << eof()
import sys
import os
import pytest

# Agregar el directorio Tarea_2 al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pregunta2 import *

@pytest.fixture
def setup():
    global GRAMMAR, INITIAL_SYMBOL, PRECEDENCES, TERMINALS, BUILD_STATUS
    """ GRAMMAR.clear()
    INITIAL_SYMBOL = None
    PRECEDENCES.clear()
    TERMINALS = [SPECIAL_SYMBOL]
    BUILD_STATUS = False """
    yield GRAMMAR, INITIAL_SYMBOL, PRECEDENCES, TERMINALS, BUILD_STATUS

def test_handle_rule_valid(setup):
    handle_rule("RULE E E + E")
    assert 'E' in GRAMMAR
    assert ['E', '+', 'E'] in GRAMMAR['E']

def test_handle_rule_invalid_non_terminal(setup):
    handle_rule("RULE e E + E")
    assert 'e' not in GRAMMAR

def test_handle_init_valid(setup):
    handle_init("INIT E")
    assert INITIAL_SYMBOL == 'E'

def test_handle_init_invalid(setup):
    handle_init("INIT e")
    assert INITIAL_SYMBOL != 'e'

def test_handle_prec_valid(setup):
    TERMINALS.extend(['n', '+'])
    handle_prec("PREC n > +")
    assert ('n', '+') in PRECEDENCES
    assert PRECEDENCES[('n', '+')] == '>'

def test_handle_prec_invalid(setup):
    TERMINALS.extend(['n', '+'])
    handle_prec("PREC n > +")
    assert ('n', '+') not in PRECEDENCES

def test_handle_build(setup):
    handle_rule("RULE E E + E")
    handle_rule("RULE E n")
    handle_init("INIT E")
    TERMINALS.extend(['n', '+'])
    handle_prec("PREC n > +")
    handle_prec("PREC + > $")
    handle_build()
    assert BUILD_STATUS

def test_handle_parse(setup):
    handle_rule("RULE E E + E")
    handle_rule("RULE E n")
    handle_init("INIT E")
    TERMINALS.extend(['n', '+'])
    handle_prec("PREC n > +")
    handle_prec("PREC + > $")
    handle_build()
    handle_parse("PARSE n + n")
    # Add assertions based on expected parse results
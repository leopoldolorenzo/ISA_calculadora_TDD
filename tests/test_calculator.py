import pytest
from src.calculator import Calculadora

def test_sumar():
    calc = Calculadora()
    assert calc.sumar(1, 2) == 3

def test_restar():
    calc = Calculadora()
    assert calc.restar(5, 2) == 3
    
def test_multiplicar():
    calc = Calculadora()
    assert calc.multiplicar(3, 2) == 6

def test_dividir():
    calc = Calculadora()
    assert calc.dividir(6, 2) == 3
    with pytest.raises(ValueError):
        calc.dividir(6, 0)
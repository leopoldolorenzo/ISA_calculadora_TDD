import pytest
from src.calculator import Calculadora

def test_sumar():
    calc = Calculadora()
    assert calc.sumar(1, 2) == 3

def test_restar():
    calc = Calculadora()
    assert calc.restar(5, 2) == 3
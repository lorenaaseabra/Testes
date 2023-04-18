import pytest
from src.calculadora import Calc, CalcError


# teste soma 3 e 4
def test_soma34():
    calculadora = Calc()
    op1 = 3
    op2 = 4
    result_calc = calculadora.soma(3, 4)
    assert result_calc == 7


# teste soma 4 e 5
def test_soma45():
    calculadora = Calc()
    op1 = 4
    op2 = 5
    result_calc = calculadora.soma(4, 5)
    assert result_calc == 9


@pytest.mark.parametrize("a, b, result_esp", [(3, 4, 7), (4, 5, 9)])
def test_soma(a, b, result_esp):
    calculadora = Calc()
    res = calculadora.soma(a, b)
    assert result_esp == res


@pytest.mark.parametrize("a, b, result_esp", [(3, "4", 7), (4, "5", 9),("100", 1, 1001)])
def test_soma_string(a, b, result_esp):
    calculadora = Calc()
    with pytest.raises(CalcError):
        res_esp = calculadora.soma(a, b)


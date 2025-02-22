import pytest
from backend.services.calc_service import calcular

def test_soma():
    assert calcular("soma", 2, 3) == 5

def test_subtracao():
    assert calcular("subtracao", 5, 3) == 2

def test_multiplicacao():
    assert calcular("multiplicacao", 3, 4) == 12

def test_divisao():
    assert calcular("divisao", 8, 2) == 4

def test_divisao_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero não permitida."):
        calcular("divisao", 5, 0)

def test_operador_invalido():
    with pytest.raises(ValueError, match="Operador inválido.*"):
        calcular("mod", 5, 2)

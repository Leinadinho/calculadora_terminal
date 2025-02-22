def calcular(operador: str, a: float, b: float):
    if operador == "soma":
        return a + b
    elif operador == "subtracao":
        return a - b
    elif operador == "multiplicacao":
        return a * b
    elif operador == "divisao":
        if b == 0:
            raise ValueError("Divisão por zero não permitida.")
        return a / b
    else:
        raise ValueError("Operador inválido. Use: soma, subtracao, multiplicacao ou divisao.")
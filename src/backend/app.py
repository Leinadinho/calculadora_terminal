import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.backend.services.calc_service import calcular

def exibir_menu():
    print("\n--- Faça seus calculos aqui ---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def main():
    while True:
        exibir_menu()
        try:
            opcao = input("Escolha uma opção (1-5): ").strip()

            if opcao == "5":
                print("Saindo...")
                break

            if opcao not in ["1", "2", "3", "4"]:
                print("Opção inválida. Tente novamente.")
                continue

            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            operador = {
                "1": "soma",
                "2": "subtracao",
                "3": "multiplicacao",
                "4": "divisao"
            }[opcao]

            resultado = calcular(operador, a, b)
            print(f"Resultado: {resultado}\n")

        except ValueError as e:
            print(f"Erro: {e}\n")
        except Exception as e:
            print(f"Erro inesperado: {e}\n")

if __name__ == "__main__":
    main()
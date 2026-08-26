def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero."
    return a / b


def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    while True:
        print("\n===== CALCULADORA =====")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            resultado = adicao(num1, num2)
            print("Resultado:", resultado)

        elif opcao == "2":
            resultado = subtracao(num1, num2)
            print("Resultado:", resultado)

        elif opcao == "3":
            resultado = multiplicacao(num1, num2)
            print("Resultado:", resultado)

        elif opcao == "4":
            resultado = divisao(num1, num2)
            print("Resultado:", resultado)

        elif opcao == "0":
            print("Calculadora encerrada!")
            break

        else:
            print("Erro: opção inválida!")


calculadora()




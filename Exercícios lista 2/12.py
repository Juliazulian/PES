menu = """Menu
-------
1 – Adição
2 – Subtração
3 – Divisão
4 – Multiplicação
0 - Sair"""

tipo = 11
while tipo != 0:
    n1=int(input("Insira o primeiro número: "))
    n2=int(input("Insira o segundo número: "))
    print("\n")
    print(menu)
    tipo = int(input("Digite a opção: "))
    print("\n")


    n1 = int(input("Digite o primeiro numero : "))
    n2 = int(input("Digite o segundo numero : "))

    match tipo:
        case 1:
            res = n1 + n2
        case 2:
            res = n1 - n2
        case 3:
            res = n1 / n2
        case 4:
            res = n1 * n2 
        case 5:
            print("Sair")

    if tipo == 1:
        res = n1 + n2
        print(f"{n1} + {n2} = {res}")
    elif tipo == 2:
        res = n1 - n2
        print(f"{n1} - {n2} = {res}")
    elif tipo == 3:
        res = n1 / n2
        print(f"{n1} / {n2} = {res}")
    elif tipo == 4:
        res = n1 * n2
        print(f"{n1} * {n2} = {res}")
    elif tipo == 0 :
        print("Sair")


# Cadastro de placas de automóveis (até 15 veículos)

placas = [None] * 15

while True:
    print("=== ESTACIONAMENTO ===")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Verifica se existe espaço disponível
        if None in placas:
            placa = input("Digite a placa do automóvel: ").upper()

            if placa in placas:
                print("Essa placa já está cadastrada.")
            else:
                indice = placas.index(None)
                placas[indice] = placa
                print("Placa cadastrada com sucesso!")
        else:
            print("Não há espaço disponível para cadastro.")

    elif opcao == "2":
        placa = input("Digite a placa que deseja excluir: ").upper()

        if placa in placas:
            indice = placas.index(placa)
            placas[indice] = None
            print("Placa excluída com sucesso!")
        else:
            print("Falha: placa não encontrada.")

    elif opcao == "3":
        print("Placas cadastradas:")
        existe = False

        for placa in placas:
            if placa is not None:
                print(placa)
                existe = True

        if not existe:
            print("Nenhuma placa cadastrada.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
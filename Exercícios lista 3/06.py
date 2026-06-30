nomes = []
idades = []
alturas = []
pesos = []
codigos = []

while True:
    print("===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Alterar")
    print("4 - Listar")
    print("0 - Sair")


    codigo = 1  

    while True:
        print("===== CADASTRO DE MEDIDAS CORPÓREAS =====")
        print("1 - Cadastrar")
        print("2 - Excluir por nome")
        print("3 - Alterar")
        print("4 - Listar")
        print("5 - Excluir por código")
        print("6 - Pesquisar por nome")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Cadastrar
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            altura = float(input("Altura (m): "))
            peso = float(input("Peso (kg): "))
            codigo = int(input("Codigo: "))

            nomes.append(nome)
            idades.append(idade)
            alturas.append(altura)
            pesos.append(peso)
            codigos.append(codigo)

            print("Cadastro realizado com sucesso!")

        elif opcao == "2":
            # Excluir
            nome = input("Digite o nome da pessoa a excluir: ")

            if nome in nomes:
                indice = nomes.index(nome)
                nomes.pop(indice)
                idades.pop(indice)
                alturas.pop(indice)
                pesos.pop(indice)
                codigos.pop(codigo)
                print("Cadastro excluído com sucesso!")
            else:
                print("Pessoa não encontrada.")

        elif opcao == "3":
            # Alterar
            nome = input("Digite o nome da pessoa a alterar: ")

            if nome in nomes:
                indice = nomes.index(nome)
                idades[indice] = int(input("Nova idade: "))
                alturas[indice] = float(input("Nova altura (m): "))
                pesos[indice] = float(input("Novo peso (kg): "))
                codigos[indice] = int(input("Novo codigo: "))
                print("Cadastro alterado com sucesso!")
            else:
                print("Pessoa não encontrada.")

        elif opcao == "4":
            # Listar
            if len(nomes) == 0:
                print("Nenhum cadastro encontrado.")
            else:
                print("=== Pessoas Cadastradas ===")
                for i in range(len(nomes)):
                    print(f"Pessoa {i + 1}")
                    print(f"Nome: {nomes[i]}")
                    print(f"Idade: {idades[i]} anos")
                    print(f"Altura: {alturas[i]:.2f} m")
                    print(f"Peso: {pesos[i]:.2f} kg")
                    print(f"Codigo: {codigos[i]:.2f}")
                
            if nome in nomes:
                indice = nomes.index(nome)
                nomes.pop(indice)
                idades.pop(indice)
                alturas.pop(indice)
                pesos.pop(indice)
                codigos.pop(codigo)
                print("Cadastro excluído com sucesso!")
            else:
                print("Pessoa não encontrada.")
                    
        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida! Tente novamente.")
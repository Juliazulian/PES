#Cria uma lista vazia de amigos proximos
amigos_proximos = []
#colocar uma variável diferente de 0 para o programa aceitar 
opcao = -1
#enquanto for diferente de 0
while opcao != 0 :
#Lista as opcoes para o usuário
    print("=== AMIGOS PROXIMOS ===")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # verifica se o amigo ja esta cadastrado
            amigo = input("Digite o nome do novo amigo: ")

            if amigo in amigos_proximos:
                print("Esse amigo ja esta na lista.")
            else:
                amigos_proximos.append(amigo)
                print("Ebaaaa, novo amigo aicionado!")

    elif opcao == 2:
        amigo = input("Digite o amigo que deseja excluir: ")

        if amigo in amigos_proximos:
            amigos_proximos.remove(amigo)
            #indice = amigos_proximos.index(amigo)
            #amigos_proximos[indice] = None
            print("Pessoa excluida com sucesso...")
        else:
            print("Falha: Este usuario não foi encontrado.")

    elif opcao == 3:
        print("AMIGOS PROXIMOS:")
        existe = False

        for amigo in amigos_proximos:
            if amigo is not None:
                print(amigo)
                existe = True

        if not existe:
            print("Voce nao tem amigos.")

    elif opcao == "0":
        print("Progama encerrado.")
        break

    
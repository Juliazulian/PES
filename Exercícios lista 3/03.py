# opcao_escolhida = -1
# while opcao_escolhida != "0":
#     print("""
# Menu
# ----
# 1 – Cadastrar
# 2 – Listar todos
# 0 – Sair 

# """)

# opcao_escolhida = input("Digite sua opção: ")

# if opcao_escolhida == "1":
#     print("Criando")

# #substituir valor se possivel
# lugar_livre = 0
# for lugar in lista:
#     if lugar > 0 :
#         break
#     lugar_livre = lugar_livre + 1

# elif opcao_escolhida == "2":
#     print("Listar")
#     for codigo in lista:
#         if codigo > 0:
#             print("Item com codigo: " codigo)




#             produtos = []

produtos = []

for i in range(10):
    produtos.append(-1)

while True:
    print("Menu")
    print("----")
    print("1 - Cadastrar")
    print("2 - Listar todos")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        codigo = int(input("Digite o código do produto: "))

        if codigo == -1:
            print("Falha! O código -1 não pode ser cadastrado.")
        else:
            sucesso = False

            for i in range(len(produtos)):
                if produtos[i] == -1:
                    produtos[i] = codigo
                    sucesso = True
                    break

            if sucesso:
                print("Cadastro realizado com sucesso!")
            else:
                print("Falha! Não há vagas disponíveis.")

    elif opcao == 2:
        print("Produtos cadastrados:")

        for codigo in produtos:
            if codigo != -1:
                print(codigo)

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")


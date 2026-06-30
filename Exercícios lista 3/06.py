nomes = []
idades = []
alturas = []
pesos = []
codigo = []

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

        opcao = int(input("Digite a opcao que deseja :"))
        if opcao == "1":
        #fazer o cadastro
            nome = input("Nome :")
            idade = int(input("Idade :"))
            altura = float(input("altura :"))
            peso = float(input("peso :"))
            codigo = int(input("codigo da pessoa :"))




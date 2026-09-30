class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso


Cadastro_de_pessoas = []

opcao = -1

while opcao != 0:

    print("\n=== CADASTRO DE PESSOAS ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))

        pessoa = Pessoa(nome, idade, altura, peso)
        Cadastro_de_pessoas.append(pessoa)

        print("Pessoa cadastrada com sucesso!")

    elif opcao == 2:
        print("\n=== CADASTRO DAS PESSOAS ===")

        if len(Cadastro_de_pessoas) == 0:
            print("A lista está vazia.")
        else:
            for pessoa in Cadastro_de_pessoas:
                print(f"Nome: {pessoa.nome}")
                print(f"Idade: {pessoa.idade}")
                print(f"Altura: {pessoa.altura}")
                print(f"Peso: {pessoa.peso}")
                print("--------------------")

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida!")


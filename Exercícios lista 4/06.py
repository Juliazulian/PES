notas = []

def media():
    media = float(0)

    for i in range(len(notas)):
        media += notas[i]
    media = media / len(notas)
    print("A media das notas do estudante é: ", media)

def cadastro():
    nota = float(input("Qual a nota do estudante? "))
    notas.append(nota)
    print("ok")

def excluir():
    nota = float(input("Digite a nota que deseja deletar:"))
    notas.remove(nota)
    print("Nota excluida")

def listar():
    print("Notas do boletim:")
    for i in range(len(notas)):
        print(notas[i])

while True:
#Lista as opcoes para o usuário
    print("=== NOTAS ===")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("4 - Calcular media")
    print("0 - Sair")

    opcao = (input("Opcao: "))

    match opcao:
        case "1":
            cadastro()
        case "2":
            excluir()
        case "3":
            listar()
        case "4":
            media()
        case "0":
            print("Programa encerrado.")
            break
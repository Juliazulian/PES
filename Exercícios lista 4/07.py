notas = []

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

def media():
    media = float(0)

    for i in range(len(notas)):
        media += notas[i]
    media = media / len(notas)
    print("A media das notas do estudante é: ", media)
    
def maior_nota():
    bolinho = notas[0]
    for i in notas: 
        if i > bolinho:
            bolinho = i
    print("A maior nota do estudante é: ", bolinho)

def menor_nota():
    cachorro = notas[0]
    for i in notas: 
        if i < cachorro:
            cachorro = i
    print("A menor nota do estudante é: ", cachorro)    

while True:
#Lista as opcoes para o usuário
    print("=== NOTAS ===")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("4 - Calcular media")
    print("5 - Mostrar maior nota")
    print("6 - Mostrar menor nota")
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
        case "5":
            maior_nota()
        case "6":
            menor_nota()
        case "0":
            print("Programa encerrado.")
            break
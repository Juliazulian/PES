dicionario = {
    "apelar" : "recorrer  a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados",
    }

for i in range(4):
    palavra = input("Digite a palavra desejada: \n-")
    significado = input("Digite o significado da palavra: \n-")
    dicionario[palavra] = significado
    print("Cadastro feito! Nova palavra adicionada! \n-")
    
    consulta_palavra = input("Qual palavra está procurando?: \n-")
    if consulta_palavra in dicionario:
        print(f"Significado: {dicionario[consulta_palavra]} \n-")
    else:
        print("Essa palavra não existe no sistema.")
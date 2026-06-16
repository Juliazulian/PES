total_caixa = 0

while True :  
    codigo = int(input("Digite o código do produto (0 para encerrar): "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade comprada: "))

    if codigo == 1:
        produto = "Suco"
        preco = 6.00
    elif codigo == 2:
        produto = "Pão de queijo"
        preco = 3.00
    elif codigo == 3:
        produto = "Pastel"
        preco = 7.00
    elif codigo == 4:
        produto = "Salada de frutas"
        preco = 9.00
    elif codigo == 5:
        produto = "Café com leite"
        preco = 3.50
    elif codigo == 6:
        produto = "Cappuccino"
        preco = 4.50
    elif codigo == 7:
        produto = "Iogurte"
        preco = 6.50
    elif codigo == 8:
        produto = "Água"
        preco = 2.50
    else:
        print("Código inválido!")
        continue

    total_compra = preco * quantidade
    total_caixa += total_compra

    print(f"Produto: {produto}")
    print(f"Valor da compra: R$ {total_compra:.2f}")

print(f"Valor total acumulado no caixa: R$ {total_caixa:.2f}")
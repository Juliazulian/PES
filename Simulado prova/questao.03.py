custo_produto = int(input("Digite o custo do produto: \n-"))
quant_produto = int(input("Digite a quantidade que você comprou: \n-"))

valor_total = custo_produto * quant_produto

if valor_total >= 100 :
    discount = valor_total * 0.10
    total = valor_total - discount
    print(f"Sua compra foi de {total} reais ")
else:
    print(f"Sua compra foi de {valor_total} reais ")
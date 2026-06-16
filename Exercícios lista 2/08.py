meses = int(input("Informe a quantidade de meses que você esta devendo: "))

if meses >= 24:
    print("Sua dívida foi quitada:")
else: 
    porcentagem = (1000*15.3)/100
    total_dividas = porcentagem*meses
    print (f"Você deve R$ {total_dividas} pro agiota. Parabéns. ")




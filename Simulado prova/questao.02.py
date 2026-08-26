cartela_bingo = []

i = 14
n = 1

while i >= 0 :
    numero = int(input(f"Digite o numero{n} desejado :"))

    if (numero <= 75 and numero >= 1) and not numero in cartela_bingo:
        cartela_bingo.append(numero)
    else:
        print("Número fora do limite permitido, digite outro :")
    i -= 1
    n+=1
cartela_bingo.sort()

print(cartela_bingo)




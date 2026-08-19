def impar_ou_par(número):
    if (número % 2) == 0 :
        return "Par"
    else:
        return "Impar"
    
número = int(input("Digite um número: "))

resultado = impar_ou_par(número)
print (resultado)
n = int(input("digite um numero : "))
numero_tabuada_inicio = int(input("digite o número inicial da tabuada : "))
numero_tabuada_fim = int(input("digite um numero final da tabuada: "))
var = numero_tabuada_inicio

while var < numero_tabuada_fim :
    resultado = var*n
    print(f"{n} x {var} = {resultado}")
    var = var + 1

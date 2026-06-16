dinheiro = float(input("Digite o valor que você deseja depositar :"))
i = float(input("Qual é a taxa de juros? (ex: 0.5% = 0.05)  "))
mes = int(input("Por quantos meses você vai guardar? "))

while mes > 24:
    print("Nosso limite é de 24 meses, insira um valor válido: ")
    mes = int(input("Por quantos meses você vai guardar? "))

M = dinheiro * (1+i)**mes

print(f"No final você terá {M: .2f}")
drone_bateria = float(input("Digite a bateria do drone de 1 a 100: \n-"))
if drone_bateria >= 70 :
    print("Pronto para voar!")
elif drone_bateria <= 69 and drone_bateria >= 30 :
    print("Voo curto recomendado...")
elif drone_bateria < 30 :
    print("Recarregue antes de voar!")
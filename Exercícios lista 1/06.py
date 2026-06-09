julia = int(input(" Escolha um dos elementos: 1 para pedra, 2 para papel ou 3 para tesoura"))
heloisa = int(input(" Escolha um dos elementos: 1 para pedra, 2 para papel ou 3 para tesoura"))

if julia == 1 and heloisa == 2 :
    print("heloisa ganhou!")
    print("julia perdeu.")
elif julia == 1 and heloisa == 3 :
    print("julia ganhou!")
    print("heloisa perdeu.")
elif julia == 1 and heloisa == 1 :
    print("Empate!")
elif julia == 2 and heloisa == 1 :
    print("julia ganhou!")
    print("heloisa perdeu.")
elif julia == 2 and heloisa == 3 :
    print("heloisa ganhou!")
    print("julia perdeu.")
elif julia == 2 and heloisa == 2 :
    print("Empate!")
elif julia == 3 and heloisa == 2 :
    print("julia ganhou!")
    print("heloisa perdeu.")
elif julia == 3 and heloisa == 1 :
    print("heloisa ganhou!")
    print("julia perdeu.")
elif julia == 3 and heloisa == 3 :
    print("Empate!") 

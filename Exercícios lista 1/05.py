temp = float(input("Qual temperatura está hoje?"))

if temp < 10 :
    print("Está muito frio! Use roupas quentes!")
elif temp >= 10 and temp <= 20 :
    print("Frio. vista-se bem!")
elif temp >= 20 and temp <= 25 :
    print("Temperatura agradável")
elif temp >= 25 and temp <= 30 :
    print("Está ficando quente!")
elif temp > 30 :
    print("Está muito quente! Fique hidratado.")
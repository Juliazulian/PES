#Crie uma função chamada tempo_total que receba a quantidade de horas e minutos
#que um jovem passou jogando videogame e retorne o total de minutos jogados. Peça ao
#usuário para inserir as horas e minutos, e exiba o tempo total em minutos

def tempo_total(tempo_horas, tempo_minutos):
    minutos_transformados = tempo_horas * 60
    total = tempo_minutos + minutos_transformados
    return total

tempo_minutos = int(input("Digite o tempo em minutos: \n-"))
tempo_horas = int(input("Digite o tempo em horas: \n-"))

print(tempo_total(tempo_horas, tempo_minutos))
      
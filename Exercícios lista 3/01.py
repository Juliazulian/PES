idades = []

# Cadastro das 6 idades
for i in range(6):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    idades.append(idade)

print("Idades maiores ou iguais a 16:")

# Exibe apenas as idades >= 16
for idade in idades:
    if idade >= 16:
        print(idade)



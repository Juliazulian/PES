# Lista para armazenar as notas
notas = []

# Leitura das 4 notas
for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

# Cálculo da média
media = sum(notas) / len(notas)

# Exibição da média
print(f"Média final: {media:.2f}")

# Situação do aluno
if media >= 6:
    print("Situação: Aprovado(a)")
else:
    print("Situação: Reprovado(a)")

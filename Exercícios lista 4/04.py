# Solicita a quantidade de cidades
quantidade = int(input("Quantas cidades deseja cadastrar no sistema? "))

# Cria uma lista vazia
cidades = []

# Faz a leitura das cidades
for i in range(quantidade):
    cidade = input(f"Digite o nome da {i + 1}ª cidade: ")
    cidades.append(cidade)

# Mostra  a lista cadastrada
print("Cidades cadastradas:")
for cidade in cidades:
    print(cidade)

# Solicita a cidade que será removida
remover = input("Digite o nome da cidade que deseja remover: ")

# Remove a cidade, se ela estiver na lista
if remover in cidades:
    cidades.remove(remover)
    print(f"A cidade '{remover}' foi removida.")
else:
    print(f"A cidade '{remover}' não foi encontrada.")

# Exibe a lista atualizada
print("Lista de cidades atualizada:")
for cidade in cidades:
    print(cidade)

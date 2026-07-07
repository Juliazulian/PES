# Lista de bairros de Garopaba

# Adicionando o primeiro bairro manualmente
bairros = ["Centro"]

# Solicitando mais 5 bairros ao usuário
for i in range(5):
    bairro = input(f"Digite o nome do {i + 2}º bairro: ")
    bairros.append(bairro)

# Exibindo todos os bairros cadastrados
print("Bairros cadastrados:")
for bairro in bairros:
    print(bairro)
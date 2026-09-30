class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    # Exibe os dados da pessoa
    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | "
            f"Altura: {self.altura}m | Peso: {self.peso}kg")

    # Calcula e exibe o IMC
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        print(f"IMC: {imc:.2f}")

    # Exibe o nome e o IMC
    def exibir_nome_imc(self):
        imc = self.peso / (self.altura ** 2)
        print(f"Nome: {self.nome} | IMC: {imc:.2f}")

pessoa1 = Pessoa("Mariana", 17, 1.60, 70)
pessoa2 = Pessoa("Schalatinha", 16, 1.20, 600)
pessoa3 = Pessoa("Zii", 16, 1.50, 300)

pessoa1.exibir_dados()
pessoa2.exibir_dados()
pessoa3.exibir_dados()

print()

pessoa1.calcular_imc()
pessoa2.calcular_imc()
pessoa3.calcular_imc()

print()

pessoa1.exibir_nome_imc()
pessoa2.exibir_nome_imc()
pessoa3.exibir_nome_imc()

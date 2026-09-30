class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def pintar(self):
        newcolor = (input("Escolha a nova cor: \n->"))
        self.cor = newcolor

    def mostrar_cor(self):
        print(f"A nova cor do carro é {self.cor}")

lamborghini = Carro("lamborghini", "cinza")

lamborghini.pintar()
lamborghini.mostrar_cor()
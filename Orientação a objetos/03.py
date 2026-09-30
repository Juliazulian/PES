class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo)

    def depositar(self):
        novo_valor = float(input("Digite um valor para adicionar ao seu saldo: R$ "))
        self.saldo += novo_valor

    def sacar(self):
        retirada = float(input("Digite um valor para retirar do seu saldo: R$ "))

        if retirada <= self.saldo:
            self.saldo -= retirada
        else:
            print("Saldo insuficiente!")

    def mostrar_saldo(self):
        print(f"O seu saldo atual é: R$ {self.saldo:.2f}")


banco = ContaBancaria("Julia", 500)

banco.depositar()
banco.sacar()
banco.mostrar_saldo()

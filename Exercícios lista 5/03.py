import math

def calcular_volume(raio, altura):
    return math.pi * raio**2 * altura

raio = float(input("Digite o raio do cilindro (em metros): "))
altura = float(input("Digite a altura do cilindro (em metros): "))

volume = calcular_volume(raio, altura)

print(f"O volume do cilindro é: {volume:.2f} m³")

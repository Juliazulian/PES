def converter(horario):
    hora, minuto = horario.split(":")
    hora = int(hora)
    minuto = int(minuto)

    if hora == 0:
        hora_convertida = 12
        periodo = "A"
    elif hora < 12:
        hora_convertida = hora
        periodo = "A"
    elif hora == 12:
        hora_convertida = 12
        periodo = "P"
    else:
        hora_convertida = hora - 12
        periodo = "P"

    return hora_convertida, minuto, periodo


def imprimir(hora, minuto, periodo):
    print(f"{hora}:{minuto:02d} {periodo}.M.")


while True:
    horario = input("Digite o horário (HH:MM): ")

    hora, minuto, periodo = converter(horario)

    imprimir(hora, minuto, periodo)

    continuar = input("Deseja fazer outra conversão? (S/N): ")

    if continuar.upper() != "S":
        break

print("Programa encerrado.")

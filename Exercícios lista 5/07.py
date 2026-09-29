# Desenha moldura. Construa uma função que desenhe um retângulo usando os
# caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas,
# sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
# valores fora da faixa forem informados, eles devem ser modificados para valores dentro
# da faixa de forma elegante.

def moldura(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    print("+" + "−" * colunas + "+")
    
    for _ in range(linhas - 2):
        print("|" + " " * colunas + "|")
    
    if linhas > 1:
        print("+" + "−" * colunas + "+")


# Exemplos
moldura(5, 10)
moldura()          # valores por omissão: 1 x 1
moldura(25, -3)    # ajustado para 20 x 1


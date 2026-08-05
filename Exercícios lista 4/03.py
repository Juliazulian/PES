#cria uma lista vazia para guardar as notas 
notas = []
#pergunta quantas notas, le e transforma em inteiro
y = int(input("Quantas notas devem ser digitadas? :"))
#repete a nota (y) vezes (quantas o usuário quiser)
for i in range(y):
    #le a nota e deixa ela ter decimais
    nota = float(input("Digite as notas :"))
    #adiciona a nota a lista
    notas.append(nota)
    #le a lista toda e mostra todas as notas
    for nota in notas:
      print(nota)
#Com while
i = 0 #começa na primeira posição da lista
while i < len(notas): # informa quantas notas existem
   print("Nota:", notas[i]) # mostra a nota na posição i
   i += 1 # passa para a próxima posição

#Com for
for nota in notas:
   print("Nota:", nota)

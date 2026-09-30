class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

Helo = Aluno("Heloisa Furio Castilho", 16)
Lucas = Aluno("Lucas Monguzzi", 16)
Zii = Aluno("Lorenzo Hubner", 16)

alunos = [Helo, Lucas, Zii]

for aluno in alunos:
    print("Aluno: ", aluno.nome, "Idade:", aluno.idade)

Zii.apresentar()
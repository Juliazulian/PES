class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def apresentar(self):
        print(f"{self.titulo} -- autor(a): {self.autor}")

Café = Livro("Antes que o café esfrie", "Toshikazu Kawaguchi")
Verity = Livro("Verity", "Colleen Hoover")
Amor = Livro("A Hipótese do amor", "Ali Hazelwood")

Café.apresentar()
Verity.apresentar()
Amor.apresentar()

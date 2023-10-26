"""2. Considere a abstração de um objeto cachorro. Crie uma classe
que possa representar as características e ações que podem ser
realizadas por esse objeto. Implemente a classe e um programa
que faça um teste demonstrativo do funcionamento da mesma."""

class Cachorro:

    raca = "pastor"
    cor = "preta"
    nome = "Lulu"

    def caracteristicaCarro(self):

        print(f"A raca máxima do cachorro é: {self.raca}")
        print(f"A cor do cachorro é: {self.cor}")
        print(f"O nome do cachorro é: {self.nome}")

cachorro = Cachorro()

cachorro.caracteristicaCarro()

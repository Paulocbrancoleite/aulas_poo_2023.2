"""1. Considere a abstração de um objeto carro. Crie uma classe que
possa representar as características e ações que podem ser
realizadas por esse objeto. Implemente a classe e um programa
que faça um teste demonstrativo do funcionamento da mesma.
"""

class Carro:

    velocidadeMaxima = "100"
    cor = "vermelho"
    marca = "Fiat"

    def caracteristicaCarro(self):

        print(f"A velocidade máxima do carro é: {self.velocidadeMaxima}")
        print(f"A cor do carro é: {self.cor}")
        print(f"O tipo do marca do carro é: {self.marca}")

carro = Carro()

carro.caracteristicaCarro()
#Escreva um programa que solicite do usuário um valor positivo e imprima
#todos os números inteiros de 1 até o número digitado pelo usuário.
x = -1
while (x<0):
    x = int(input("Digite um número inteiro positivo: "))

for i in range(1, x +1):
        print(i, end=" ")

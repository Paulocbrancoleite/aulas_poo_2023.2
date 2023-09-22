#Escreva um programa que solicite do usuário dois valores positivos e
#imprima todos os números inteiros dentro desse intervalo excluindo-se o
#valor inicial do intervalo e o valor final.

v_ini = -1
v_fim = -1
while (v_ini < 0 and v_fim < 0):
    v_ini = int(input("Digite um número inteiro positivo: "))
    v_fim = int(input("Digite um número inteiro positivo: "))


    for i in range(v_ini -1, v_fim):
        print(i, end=" ")
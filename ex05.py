"""
O cálculo do fatorial de um número é dado pela multiplicação desse
número com todos os antecessores inteiros positivos. Por exemplo, o
fatorial de 5 é 5! = 5*4*3*2*1 = 120. Escreva um programa que
solicite um número e apresente o resultado do seu fatorial."""

x = -1
fatorial = 1
while (x<0):
    x = int(input("Digite um inteiro maior que zero: "))

for i in range(1, x+1):
    fatorial *= i
    print(f"{i}! = {fatorial}")

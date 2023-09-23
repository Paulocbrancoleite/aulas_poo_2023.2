"""Escreva um programa que recebe como entrada um valor de temperatura e
como resultado imprime uma mensagem conforme descrito. Se a temperatura
estiver abaixo de 15oC - ‘Aqui não é o RN’; se estiver entre 16oC e 25oC -
‘Pense num frio’; se estiver entre 26oC e 30oC - ‘Temperatura normal e super
agradável’; se estiver entre 31oC e 35oC - ‘Tá quente pra danado’; se estiver
acima de 35oC - ‘Calor da muléstia!’. O programa deverá perguntar ao usuário
a temperatura atual e exibir a mensagem. Enquanto o usuário não digitar um
valor negativo para a temperatura o programa deve continuar executando."""

temperatura_atual = int(input("Digite a temperatura altual do ambiente: "))

if (temperatura_atual > 0):
    if (temperatura_atual <= 15):
        print("Aqui não é o RN!")
    elif (temperatura_atual >= 16 and temperatura_atual <= 25):
        print("Pense num frio!")
    elif (temperatura_atual >=26 and temperatura_atual <= 30):
        print("Temperatura normal e super agradável!")
    elif (temperatura_atual >= 31 and temperatura_atual <= 35):
        print("Tá quente pra danado!")
    else:
        print("Calor da muléstia!")
else:
    print("O RN não é Sibéria, Galado!")

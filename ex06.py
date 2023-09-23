"""Escreva um programa para fazer uma pesquisa de opinião sobre a
satisfação no atendimento de uma farmácia. As opções de respostas
devem ser INSATISFEITO; SATISFEITO; NÃO QUERO RESPONDER. O
algoritmo deverá ainda perguntar quantas usuários irão responder à
pergunta. Ao final apresentar o percentual de resposta de cada opção."""

quantidade_usuarios = int(input("Digite a quantidade de usuários que responderam as perguntas: "))
insatisfeito = 0
satisfeito = 0
nao_respondeu = 0

for i in range (quantidade_usuarios):
    resposta = int(input("Digite 0 para INSATISFEITO.\n Digite 1 para SATISFEITO. \n Digite qualquer outro inteiro para NÃO QUERO RESPONDER.")) 
    if (resposta == 0):
        insatisfeito += 1
    elif (resposta == 1):
        satisfeito += 1
    else:
        nao_respondeu += 1

print(f"O percentual de insatisfeitos é: {(insatisfeito * 100) / quantidade_usuarios}%")
print(f"O percentual de satisfeitos é: {(satisfeito * 100) / quantidade_usuarios}%")
print(f"O percentual de entrevistados que não responderam é: {(nao_respondeu * 100) / quantidade_usuarios}%")

"""Aula 05 - break e continue em loops"""

# break é usado para sair de um loop antecipadamente

for i in range(10):
    if i == 4:
        print('Break acionado em i =', i)
        break  # Sai do loop quando i é igual a 5
    print('Valor de i:', i)

# encontrar a posição de um numero em uma lista de inteiros
# se o numero não existir, retornar -1

busca = 5
numeros = [1, 4, 9, 7, 5, 3, 2, 1, 7]
posicao = -1
contador = 0
# for numero in numeros:
#     print('Procurando na posicao', contador)
#     if numero == busca:
#         posicao = contador
#         break
#     contador += 1

# print(posicao)

for i in range(len(numeros)):
    print('Procurando na posicao', contador)
    if numeros[i] == busca:
        posicao = contador
        break

print(posicao)


# continue é usado para pular a iteração atual e continuar com a próxima

for numero in numeros:
    if numero == 3:
        print('Continue acionado para o número 3')
        continue  # Pula o restante do código no loop quando o número é 3
    print('Número atual:', numero)

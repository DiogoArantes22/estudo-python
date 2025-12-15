"""Aula 03 - loop for"""
# Loop for é usado para iterar sobre uma sequência (como listas, tuplas, strings), repetir instruções para cada item na sequência

linguagens = ['C', 'Python', 'Java']

print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

for linguagem in linguagens:
    print('Linguagem:', linguagem.upper())  # .upper() converte a string para maiúsculas

#Comportamento do operador in é diferente com base no contexto
print('Java' in linguagens)  # Verifica se 'Java' está na lista

#Contar elementos em uma coleção
nota1 = 10.0
nota2 = 5.5
nta3 = 8.3

media = (nota1 + nota2 + nta3) / 3
print('Média:', media)

notas = [10.0, 5.5, 8.3]
soma = 0.0

for nota in notas:
    soma += nota  # soma = soma + nota
    
media = soma / len(notas)  # len() retorna o número de elementos na lista
print('Média calculada com loop:', media)

#Range - gera uma sequência de números inteiros
#valores = range(0,10)  # Gera números de 0 a 10
valores = range(0,10,2)  # Gera números de 0 a 10 de 2 em 2

print(valores)
for valor in valores:
    print('Valor do range:', valor)
    
    
for linguegem in range(len(linguagens)):
    print('Linguagem do range:', linguagens[linguegem])

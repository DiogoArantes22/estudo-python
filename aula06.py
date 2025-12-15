"""Aula06 - Conversoes de tipos"""

# Conversão implícita de tipos

leitura = 5.53
peso = 3

total = leitura * peso  # o Python converte 'peso' de int para float automaticamente
print("Total (conversão implícita):", total, type(total))

# Conversão explícita de tipos (typing casting)

#soma = 13.4 + '3.5' # Isso causará um erro de tipo

soma = 13.4 + float('3.5')  # Convertendo a string '3.5' para float antes da soma
print("Soma (conversão explícita):", soma, type(soma))

nome = 'Diogo'
altura = 1.84

mensagem = nome + ' tem ' + str(altura) + ' metros de altura.'  # Convertendo float para string
print(mensagem)
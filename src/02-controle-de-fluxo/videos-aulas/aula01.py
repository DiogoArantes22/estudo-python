"""Aula 01 - Operadores """

# Operadores são símbolos especiais que realizam operações em valores e variáveis

# Operadores Aritméticos
print('1 + 1', 1 + 1, type(1 + 1))  # Adição
print('5 - 2', 5 - 2, type(5 - 2))  # Subtração
print('3 * 4', 3 * 4, type(3 * 4))  # Multiplicação
print('10 / 2', 10 / 2, type(10 / 2))  # Divisão (resultado é float)
print('10 // 3', 10 // 3, type(10 // 3))  # Divisão inteira (resultado é int)
print('2 ** 3', 2 ** 3, type(2 ** 3))  # Exponenciação

#Operadores de atribuição
x = 10  # Atribuição simples
print('x =', x)

#Operadores de comparação
resultado = x > 10   # Maior que
print('x > 10:', resultado, type(resultado))
resultado = x < 10   # Menor que
print('x < 10:', resultado, type(resultado))
resultado = x >= 10  # Maior ou igual a
print('x >= 10:', resultado, type(resultado))
resultado = x <= 10  # Menor ou igual a
print('x <= 10:', resultado, type(resultado))

print('x == 10:', x == 10, type(x == 10))  # Igual a

print('x != 10:', x != 10, type(x != 10))  # Diferente de

#Operadores relacionais
resultado_consicao = x > 10 and x < 20  # E lógico

#Operadores lógicos
print('true and true:', True and True, type(True and True)) # E lógico
print('true and false:', True and False, type(True and False)) # 
print('false and false:', False and False, type(False and False)) 
print('false and true:', False and True, type(False and True)) 

print('true or true:', True or True, type(True or True)) # OU lógico
print('true or false:', True or False, type(True or False)) 
print('false or false:', False or False, type(False or False))
print('false or true:', False or True, type(False or True))

print('not true:', not True, type(not True))  # Negação lógica
print('not false:', not False, type(not False))

#Operadores especiais

#is (verifica se dois objetos são o mesmo na memória)
a = 10
b = 10.0
c = b

print(a==b, a==c, b==c)  # Compara valores
print(a is b, a is c, b is c)  # Compara identidades

#in (verifica se um valor está presente em uma coleção)
frase = 'Voce é um palavrão!'
print('palavrão' in frase, type('palavrão' in frase))  # Verifica se a substring está na string
print('Palavrão' in frase, type('palavrão' in frase))

numero = [1, 2, 3, 4, 5]
print(1 in numero, type(3 in numero))  # Verifica se o número está na lista
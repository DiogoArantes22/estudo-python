"""Aula03 -  (set)"""
# Sets (conjuntos)


# criando um conjunto
# conjuntos não permitem valores duplicados
numeros = {12, 1, 5, 7, 4, 3, 3, 1}
print(numeros, type(numeros))

# acessando elementos do conjunto
for numero in numeros:
    print(numero)

# verificando se um elemento está no conjunto
print(5 in numeros)  # True
print(10 in numeros)  # False

# adicionando elementos ao conjunto
numeros.add(10)
print(numeros)

# adcionar elementos de outro conjunto
numeros2 = {15, 20, 25}

# todos_numeros = numeros.update(numeros2)  #Error: o método update não retorna um novo conjunto, ele modifica o conjunto original
# print(numeros, type(numeros))

# adiciona os elementos de numeros2 ao conjunto numeros
numeros.update(numeros2)
print(numeros, type(numeros))
print(numeros2, type(numeros2))

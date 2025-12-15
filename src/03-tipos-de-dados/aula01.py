"""Aula 01 - listas em Python."""
# listas em Python são coleções ordenadas e mutáveis de itens.

# criando uma lista
nomes = ['Diogo', 'Maria', 'João']

# acessando elementos da lista
print(nomes, type(nomes))

print(nomes[0:2])  # acessando elementos da lista com range

print(nomes[:2])  # acessando elementos do início até o índice 2 (exclusivo)

print(nomes[1:])  # acessando elementos do índice 1 até o final da lista

# modificando elementos da lista
nomes[0] = 'Diogo Arantes'
nomes[1:] = ['Ana', 'Carlos']  # modificando uma fatia da lista
print(nomes)

# tamnho da lista
print(len(nomes))
# adicionando elementos à lista
nomes.append('Beatriz')  # adiciona um elemento ao final da lista
print(nomes)

# metodo insert
nomes.insert(1, 'Fernando')  # adiciona um elemento na posição especificada
print(nomes)

# metodo extend
nomes2 = ['Juliana', 'Pedro']
nomes.extend(nomes2)  # adiciona os elementos de outra lista ao final da lista
print(nomes)

# removendo elementos da lista
nomes.remove('Ana')  # remove a primeira ocorrência do valor especificado
print(nomes)

# del para remover um elemento pelo índice
del nomes[2]  # remove o elemento na posição especificada
print(nomes)

# remove da memoria a lista inteira
del nomes
print(nomes)

# limpar a lista sem deletar a variável
nomes = ['Diogo', 'Maria', 'João']
nomes.clear()  # remove todos os elementos da lista

# interação com a lista
for nome in nomes2:
    print(nome)

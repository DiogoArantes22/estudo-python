"""Aula02 - Tuplas em Python"""
# tuplas em Python são coleções ordenadas e imutáveis de itens.

nomes = ('Diogo', 'Maria', 'João')
print(nomes, type(nomes))

#acessando elementos da tupla
print(nomes[0:2])  # acessando elementos da tuplas com range

print(nomes[:2])  # acessando elementos do início até o índice 2 (exclusivo)

print(nomes[1:])  # acessando elementos do índice 1 até o final da tuplas 

#modificando elementos da tupla - não é possível, pois tuplas são imutáveis

#interação com a tupla
for nome in nomes:
    print(nome)
    
for i in range(len(nomes)):
    print(nomes[i])
    
    
nomes2 = 'Ana', 'Carlos'  # criando uma tupla sem parênteses
print(nomes2, type(nomes2))

#unpack colocando os valores da tupla em variáveis
# nome1 = nomes2[0]
# nome2 = nomes2[1]

nome1, nome2 = nomes2  # forma de unpack
print(nome1)
print(nome2)

#juntar duas tuplas
todos_nomes = nomes + nomes2
print(todos_nomes, type(todos_nomes))
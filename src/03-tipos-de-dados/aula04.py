"""Aula 4 - Dicionários"""
# Dicionários em Python são coleções não ordenadas, mutáveis e indexadas por chaves e valor.

# criando um dicionário
carro = {
    'marca': 'Ford',
    'modelo': 'Mustang',
    'ano': 1964
}
print(carro, type(carro))
# acessando elementos do dicionário
print(carro['marca'])  # acessando o valor pela chave
print(carro.get('modelo'))  # acessando o valor pela chave usando o método get

# acessar todas as chaves do dicionário
print(carro.keys())

# acessar todos os valores do dicionário
print(carro.values())

# acessando pares chave-valor do dicionário
print(carro.items())

# verificar se uma chave está no dicionário
print('marca' in carro)  # True
print('cor' in carro)    # False

# adicionando elementos ao dicionário
carro['cor'] = 'vermelho'
print('cor' in carro)  # True
print(carro)

# removendo a chave
marca = carro.pop('marca')  # remove o par chave-valor pela chave
print(carro)
print('Marca removida:', marca)

# Loop no dicionário
for key in carro:
    print(key, carro[key], type(key))

for value in carro.values():  # acessando apenas os valores
    print(value)

for key in carro.keys():  # acessando apenas as chaves
    print(key)

for key, value in carro.items():  # acessando chave e valor
    print(key, value)

# lista de dicionários
aluno1 = {
    'nome': 'Diogo',
    'email': 'Diogo@email.com'
}
aluno2 = {
    'nome': 'Maria',
    'email': 'maria@email.com'
}

alunos = [aluno1, aluno2]

for aluno in alunos:
    print('nome:', aluno['nome'], 'email:', aluno['email'])

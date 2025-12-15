"""aula 05 tipos de dados"""

# Numéricos
inteiro = 10          # Tipo int
flutuante = 10.5     # Tipo float

print("Inteiro:", inteiro, type(inteiro))
print("Flutuante:", flutuante, type(flutuante))

# Strings
nome = 'Diogo'
sobrenome = 'Arantes'
nome_completo = nome + ' ' + sobrenome  # Concatenação de strings
print("Nome completo:", nome_completo, type(nome_completo))

# Interpolação de strings (f-strings)
produto = 'notebook'

print(f"{nome_completo} comprou um {produto} por R$ 2500,00.")

# O tipo string no python é tipo lista de caracteres
# Acessa o primeiro caractere da string
print("Primeira letra do nome:", nome[0])

# booleanos
verdadeiro = True
falso = False

print(True, type)

resultado = 10 < 3
print("Resultado da comparação 10 < 3:", resultado, type(resultado))

# Listas
frutas = ['maçã', 'banana', 'laranja']
print("Frutas:", frutas, type(frutas))

print(frutas[0])  # Acessa o primeiro elemento da lista
print(frutas[1])  # Acessa o segundo elemento da lista
print(frutas[2])  # Acessa o terceiro elemento da lista

# adicionar um elemento no final da lista
frutas.append('uva')
print("Frutas após append:", frutas)

# Saber quantos elementos tem na lista
print("Número de frutas na lista:", len(frutas))

# varrer a lista com loop
for fruta in frutas:
    print("Fruta:", fruta)


# Tuplas (imutáveis)
codigos = (1001, 1002, 1003)

print("Códigos:", codigos, type(codigos))

# Conjuntos (sets) - não permitem elementos duplicados
numeros = {1, 2, 3, 4, 5, 5, 5}  # O número 5 será armazenado apenas uma vez
print("Números (set):", numeros, type(numeros))

# Dicionários (dict) - estrutura de chave-valor
funcionario = {
    'codigo': 101,
    'nome': 'Diogo Arantes',
    'salario': 3500.00
}
print("Funcionário:", funcionario, type(funcionario))
# Acessa o valor associado à chave 'nome'
print("Nome do funcionário:", funcionario['nome'])

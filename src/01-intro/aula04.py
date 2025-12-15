"""Aula 04 - Variáveis, contantes e literais em Python"""
# Variáveis são usadas para armazenar valores que podem mudar durante a execução do programa

# Variaveis container para guardar dados
#Interferencia de tipos: Python é uma linguagem de tipagem dinâmica, ou seja, você não precisa declarar o tipo da variável explicitamente
#O interpretador do Python infere o tipo da variável com base no valor atribuído a ela
numero = 10 # variável do tipo inteiro
print("Número:", numero)
print(type(numero))  # Saída: <class 'int'>, type() mostra o tipo da variável

numero = 15.5 # agora a variável 'numero' armazena um valor do tipo float
print("Número:", numero)

#multipls atribuições (não muito usada, mas é possível)
nome, idade, endereco = "Ana", 30, "Rua A, 123"
print(nome, idade, endereco)

#atribui o mesmo valor para múltiplas variáveis
a = b = c = 100
print(a, b, c)

#sanake_case: convenção de nomenclatura onde as palavras são separadas por underscores (_)
salario_atual = 2500.75

#Constantes são valores que não mudam durante a execução do programa
#Em Python, não há uma sintaxe específica para declarar constantes, mas por convenção, usamos letras maiúsculas para nomeá-las

PI = 3.14
MAIORIDADE = 18

#literais são valores fixos que são diretamente inseridos no código-fonte
#Exemplos de literais: números (inteiros e floats), strings, booleanos, listas, tuplas, dicionários, etc.
idade = 25  # 25 é um literal inteiro
preco = 19.99  # 19.99 é um literal float
nome = "Carlos"  # "Carlos" é um literal string
ativo = True  # True é um literal booleano
# None é um literal especial que representa a ausência de valor

#Coleções como literais

#Lista
numeros = [1, 2, 3, 4, 5]  # lista de inteiros

#Tupla (tuplas são imutáveis)
emails = ('diogo@email.com', 'fulano@email.com')  # tupla de strings

#Conjunto (set) (nao permite elementos duplicados)
letras = {'a', 'b', 'c', 'd'}  # conjunto de caracteres
print("Letras:", letras, type(letras))

#Dicionário (dict) (estrutura de chave-valor)
pessoa = {'nome': 'Ana', 'idade': 28, 'cidade': 'São Paulo'}  
# dicionário com informações de uma pessoa
print("Pessoa:", pessoa, type(pessoa))
"""Aula07 - Entrada e Saída de Dados em Python."""
# Entrada de dados com a função input()

# saida padrap - sys stdout
print('Hello, World!', 'Diogo', sep='-', end='!!!\n')

# arquivos
arquivo = open('nomes.txt', 'w', encoding='utf-8')

print('Diogo', 'Maria', 'Pedro', file=arquivo, sep='; ', end='.\n')


# Entrada de dados do usuário
nome = input("Digite seu nome: ")
# Convertendo a entrada de idade para inteiro
idade = int(input("Digite sua idade: "))
idade = int(idade)  # Convertendo a idade de string para inteiro
print("Olá,", nome + "! Você tem", idade, "anos.")

# Arquivo como fonte de entrada de dados

arquivo = open('nomes.txt', 'r', encoding='utf-8')
conteudo = arquivo.read()

print(conteudo)

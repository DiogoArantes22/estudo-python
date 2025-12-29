""""Aula 04 - funções em Python"""
#Função é um bloco de código reutilizável que realiza uma tarefa específica.
#Evita duplicação de código e melhora a organização do programa.

#1. Standard Library Functions - built-in functions
#Exemplos: print(), len(), type(), int(), str(), float(), input()

print("Ola", 123, True)  # Imprime uma mensagem na tela

nomes = ['João', 'Maria']
tamanho_lista = len(nomes)  # Retorna o tamanho da lista

print(nomes, tamanho_lista)

#2. User-defined Functions - funções definidas pelo usuário
#Definimos nossas próprias funções usando a palavra-chave def.

#decklarando a função
#nome : saudacao
#parâmetros: nenhum
#retorno: nenhum
def saudacao():
    """Função que imprime uma saudação"""
    print("Olá! Bem-vindo")
#chamando a função
saudacao()

#Função com parâmetros
#nome: saudacao_nome
#parâmetros: nome (str)
#retorno: nenhum
def saudacao_nome(nome):
    """Função que imprime uma saudação personalizada"""
    print(f"Olá, {nome}! Bem-vindo")
  
#chamando a função com argumento  
saudacao_nome("Diogo")
saudacao_nome("Ana")
nome = 'Carlos'
saudacao_nome(nome)

#Função com retorno
#nome: calcular_media
#parâmetros: nota1 (float), nota2 (float), nota3 (float
#retorno: média (float)
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(f"A média é: {media}")
    return media

#chamando a função e armazenando o retorno
#argumentos literal
media = calcular_media(10.0, 3.0, 6.0)
n1 = 10.0
n2 = 3.0
n3 = 8.0
#argumentos por variável
calcular_media(n1, n2, n3)
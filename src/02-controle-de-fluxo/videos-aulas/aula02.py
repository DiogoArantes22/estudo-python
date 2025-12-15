"""Aula 02 - if"""
# Estrutura condicional if é usada para executar um bloco de código se uma condição for verdadeira

valor_desconto = 30.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

if DESCONTO_ESPECIAL:
    print("Desconto especial aplicado!")
    preco_final = 100.0 - valor_desconto
    print("Preço final com desconto:", preco_final)
else:
    print('Sem desconto especial.')

# Nome tem que ter pelo menos 3 caracteres
nome = 'Lo'

NOME_INVALIDO = len(nome) < 3

if NOME_INVALIDO:
    print('Nome deve ter pelo menos 3 caracteres')
else:
    print('Nome válido:', nome)

NOME_VALIDO = len(nome) >= 3

if NOME_VALIDO:
    print('Nome válido:', nome)
else:
    print('Nome deve ter pelo menos 3 caracteres')

if not NOME_INVALIDO:
    print('Nome válido:', nome)
else:
    print('Nome deve ter pelo menos 3 caracteres')

# Idade tem que ser maior ou igual a 18 anos
# Nome tem que ter pelo menos 3 caracteres
# Exibir todos os erros no final
nome = 'Lo'
idade = 17
altura = 172
erros = []

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append('Nome deve ter pelo menos 3 caracteres')

IDADE_INVALIDA = idade < 18
if IDADE_INVALIDA:
    erros.append('Idade deve ser maior ou igual a 18 anos')

# Para saber se é false usa-se: False, 0, "", [], {}, (), None
# Para saber se é true usa-se: True, qualquer valor diferente de 0, qualquer string não vazia, listas, dicionários ou tuplas com elementos
if len(erros) != 0:
    print(erros)
else:
    print('Nome e idade válidos:', nome, idade)


# Verifica se o numero é positivo, negativo ou zero
numero = 2
if numero > 0:
    print('Número positivo')
elif numero < 0:
    print('Número negativo')
else:
    print('Número é zero')


# Calcule a media e verifique se as duas notas são válidas antes do calculo

n1 = 5.6
n2 = 10.0

NOTA1_VALIDA = 0 <= n1 <= 10
NOTA2_VALIDA = 0 <= n2 <= 10

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2) / 2
    print('Média:', media)
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('Notas inválidas')

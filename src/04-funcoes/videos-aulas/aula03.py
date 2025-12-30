"""Aula 03 - Arguments: *args e **kwargs"""

# *args - argumentos posicionais variáveis
#Não precisamos necessáriamente chamar os parâmetros de *args assim, mas é uma convenção.

#função imprime nome do pais e quantas copas do mundo ganhou
#nome: world_cup_titles
#parâmetros: country (str), *args (int)
#retorno: nenhum
def world_cup_titles(country, *args):
    print('Country: ', country)
    for title in args:
        print('year: ', title)

#Com *args podemos iterar sobre um número variável de argumentos posicionais, ou sjea, podemos passar quantos argumentos quisermos.
world_cup_titles('Brasil', 1958, 1962, 1970, 1994, 2002)
world_cup_titles('Alemanha', 1954, 1974, 1990, 2014)
world_cup_titles('Espanha', 2010)

# **kwargs - argumentos nomeados variáveis
#Não precisamos necessáriamente chamar os parâmetros de **kwargs assim, mas é uma convenção

#Usado para passar um número variável de argumentos nomeados (keyword arguments) para uma função.

#Função de cálculo de preço com dois argumentos opcionais. 
# Desconto e texa de imposto
#nome: calcular_preco
#parâmetros: valor (float), **kwargs
#retorno: preço final (float)
def calcular_preco(valor, **kwargs):
    taxa_percentual = kwargs.get('taxa_percentual')
    desconto = kwargs.get('desconto')
    if taxa_percentual:
        valor += valor * (taxa_percentual / 100)
    if desconto:
        valor -= desconto
    return valor

#Chamando a função sem argumentos opcionais
preco_final = calcular_preco(100.0)

#Aplicando apenas o desconto
preco_final = calcular_preco(100.0, desconto = 5.0) 

#Aplicando apenas a taxa percentual
preco_final = calcular_preco(100.0, taxa_percentual = 7)

#Aplicando ambos os argumentos opcionais
preco_final = calcular_preco(100.0, taxa_percentual = 7, desconto = 5.0)

# Diferença entre *args e **kwargs
# *args é usado para passar um número variável de argumentos posicionais para uma função.
# **kwargs é usado para passar um número variável de argumentos nomeados para uma função. Qualquer combinação de ambos pode ser usada em uma única função, desde que *args venha antes de **kwargs na definição da função.
def exemplo_completo(*args, **kwargs):
    print("Argumentos posicionais (args):", args)
    print("Argumentos nomeados (kwargs):", kwargs)
exemplo_completo(1, 2, 3, nome="Diogo", idade=23)
"""Aula 02 - Arguments: positional , keyword e default values"""

#declara uma função que soma dois números
def somar(n1, n2):
    return n1 + n2

def dividir(dividendo, divisor):
    """Função que divide dois números, com valor padrão para o divisor"""
    return dividendo / divisor
#chamando a função com argumentos posicionais
print(somar(10, 3.5))  # argumentos posicionais
print(somar(2.0, 6.5))
print(dividir(10.0, 2.0))  # argumentos posicionais


#unpack list e tuplas
numeros = [10.0, 5.5]
# desempacotando lista como argumentos posicionais
print('somar numeros de uma list',somar(numeros[0], numeros[1]))  
# desempacotando lista como argumentos posicionais
print('somar numeros de uma list com *',somar(*numeros))  

#unpack dicionários
numeros =  {'n1': 10.2, 'n2': 5.3}

print('somar numeros de um dict com **',somar(**numeros))

#chamando a função com argumentos nomeados (keyword arguments)
print(somar(n2=4.5, n1=7.5))  # ordem dos argumentos não importa
print(somar(n1=1.0, n2=2.0))
print(dividir(divisor=3.0, dividendo=10.0))  # argumentos nomeados

#defult values
#declaração
#nome: saudacoes
#parâmetros: nome (str), saudacao (str, default="Olá")
#retorno: string
def saudacoes(nome, saudacao = 'Oi'):
    """Função que retorna uma saudação personalizada com valor padrão"""
    return f"{saudacao} {nome}"

#chamando a função com e sem o argumento padrão
print(saudacoes("Diogo", "Olá"))  # sem valor padrão
print(saudacoes("Maria", "Bom dia"))  # sem valor padrão
print(saudacoes("Pedro"))  # com valor padrão

print(saudacoes(saudacao="Saudações", nome="Carlos"))  # sem valor padrão e argumento nomeado
print(saudacoes(nome="Ana"))  # com valor padrão e argumento nomeado

"""ex03.py: Crie uma função que recebe uma tupla de números como 
parâmetro (numeros) e retorna a soma desses números.  """


def soma_numeros_tupla(numeros):
    return sum(numeros)


tupla_numeros = (10, 20, 30, 40, 50)
resultado = soma_numeros_tupla(tupla_numeros)
print("A soma dos números na tupla é : ", resultado)

numeros = input("Digite números separados por vírgula: ")
tupla_numeros = tuple(float(num) for num in numeros.split(','))

print("A soma dos números na tupla é : ", soma_numeros_tupla(tupla_numeros))

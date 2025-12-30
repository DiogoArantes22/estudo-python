"""ex02.py: Crie uma função que recebe três números como parâmetro (n1, n2, n3) e retorna a soma dos números.  """


def soma_tres_numeros(n1, n2, n3):
    return n1 + n2 + n3


resultado = soma_tres_numeros(10, 20, 30)
print("A soma dos três números é : ", resultado)

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
resultado = soma_tres_numeros(n1, n2, n3)
print("A soma dos três números é : ", resultado)

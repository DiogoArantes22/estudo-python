"""ex01.py: Crie uma função que recebe três números como parâmetro (n1, n2, n3) e imprime na saída padrão a soma dos números."""


def soma_tres_numeros(n1, n2, n3):

    print("A soma dos três números é : ", n1 + n2 + n3)


soma_tres_numeros(10, 20, 30)

n1 = float(input("Digite o primeiro número: "))
n2 =float(input("Digite o segundo número: "))
n3 =float(input("Digite o terceiro número: "))
soma_tres_numeros(n1, n2, n3)

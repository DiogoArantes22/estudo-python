""" ex04.py:  Crie uma função que recebe vários argumentos numéricos através de *args e retorna a soma dos números."""

def soma_varios_numeros(*args):
    return sum(args)

resultado = soma_varios_numeros(10, 20, 30, 40, 50)
print("A soma dos números é : ", resultado)


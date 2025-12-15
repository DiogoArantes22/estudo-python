""" ex01.py  
○ Solicite ao usuário 3 números.  
○ Armazene os valores em uma lista.  
○ Ao final, apresente o menor e o maior elemento.  """

numeros = []

for i in range(3):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)

print("Menor número:", menor)
print("Maior número:", maior)

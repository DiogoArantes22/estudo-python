"""EXERCICIO 1

ex01.py: solicite ao usuário 3 notas e apresente o resultado da média 
aritmética.  

"""
# ex01.py

notas = []

while len(notas) < 3:
    nota = float(input("Digite uma nota entre 0 e 10: "))

    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida! Digite um valor entre 0 e 10.")

media = sum(notas) / len(notas)

print("Média:", media)



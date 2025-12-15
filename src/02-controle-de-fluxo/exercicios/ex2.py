"""ex2 

 ex02.py: solicite ao usuário, uma única vez, as notas no formato n1, n2, n3, 
nm e apresente:  
○ a média aritmética das notas;  
○ a situação: aprovado (média > 6.0), recuperação (4.0 ≤ média ≤ 6.0) ou 
reprovado (média < 4.0).  
○ Dicas:  
■ Use o método split da classe str para obter uma lista de notas.  
■ O programa deve funcionar para qualquer quantidade de notas 
(ex.: 10.0, 3.0 ou 10.0, 3.0, 2.0, 5.6, 8.2). """

entrada = input("Digite as notas separadas por vírgula (ex: 7, 8, 6): ")

notas_texto = entrada.split(",")
notas = []

for nota in notas_texto:
    notas.append(float(nota))

media = sum(notas) / len(notas)

print("Média:", media)

if media > 6:
    print("Situação: Aprovado")
elif media >= 4:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")

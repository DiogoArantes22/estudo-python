"""Aula 01 - Debug em Python"""

def somar(n1,n2,n3):
    soma = n1 + n2 + n3
    return soma

def calcular_media(n1, n2, n3):
    soma = somar(n1, n2, n3)
    media = soma / 3
    return media



nota1 = 10.0
nota2 = 3.0
nota3 = 5.5

breakpoint()  # Ponto de interrupção para depuração

media = calcular_media(nota1, nota2, nota3)
print(f"A média das notas é: {media}")

#comanddos uteis para depuração:
#c - continuar
#n - próximo
#s - entrar na função
#l - listar código
#p - printar variável
#q - sair do depurador
#help - ajuda do depurador
#next - próxima linha
#step - entrar na função
#list - listar código
#return - continuar até o retorno da função atual
#jump linha_numero - pular para a linha especificada
#whatis variável - mostrar o tipo da variável
#args - mostrar os argumentos da função atual
#break linha_numero - definir um ponto de interrupção na linha especificada
#clear linha_numero - remover o ponto de interrupção da linha especificada
#EOF - fim do arquivo
#exit - sair do depurador
#quit - sair do depurador
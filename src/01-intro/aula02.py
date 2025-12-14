""""aula 02- Keywords e identificadores"""

#Palavras reservadas (keywords) não podem ser usadas como identificadores
#Exemplos de keywords: False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except,
#finally, for, from, global, if, import, in, is, lambda,

#identificadores são os nomes que damos para variáveis, funções, classes, etc.
#Regras para criar identificadores:
#1. Devem começar com uma letra (a-z, A-Z) ou um underscore (_)
#2. Podem conter letras, dígitos (0-9) e underscores (_)
#3. Não podem conter espaços ou caracteres especiais (como !, @, #, $, %, etc.)
#4. Não podem ser iguais a palavras reservadas (keywords)

nome = "João"
idade = 25
Nome = "Maria"  # Diferente de 'nome' (case sensitive)
nome_completo = "João Silva"  # Uso de underscore para separar palavras

#boa prática: usar nomes descritivos para identificadores
c = 10  # ruim
contador = 10  # bom

s = 10 + 5  # ruim
soma = 10 + 5  # bom

#Constantes em Python são geralmente escritas em maiúsculas

PI = 3.14
MAIORIDADE = 18
if idade >= MAIORIDADE:
    print("é maior de idade.")
else:
    print("é menor de idade.")
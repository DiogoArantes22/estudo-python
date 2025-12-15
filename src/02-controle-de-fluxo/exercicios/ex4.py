"""ex04
ex04.py: baseado no ex03.py, ao final do programa apresente todas as 
inconsistências do identificador informado (use uma list de erros). 
Exemplos:  
○ Entrada: B9999999X  
■ Erros:  
● O identificador não inicia com a sequência BR.  
● O identificador não apresenta número inteiro entre 0001 
e 9999.  
○ Entrada: BR9999Y  
■ Erros:  
● O identificador não finaliza com o caractere X. 

"""

identificador = input("Digite o identificador: ")

erros = []

if not identificador.startswith("BR"):
    erros.append("O identificador não inicia com BR.")

if not identificador.endswith("X"):
    erros.append("O identificador não termina com X.")

if len(identificador) != 7:
    erros.append("O identificador não possui 7 caracteres.")

if len(identificador) >= 6:
    numero = identificador[2:6]

    if not numero.isdigit():
        erros.append("O identificador não possui número válido.")
    else:
        numero_int = int(numero)
        if numero_int < 1 or numero_int > 9999:
            erros.append("O número deve estar entre 0001 e 9999.")
else:
    erros.append("O identificador não possui número válido.")

if len(erros) == 0:
    print("Identificador válido.")
else:
    print("Identificador inválido. Erros encontrados:")
    for erro in erros:
        print("-", erro)

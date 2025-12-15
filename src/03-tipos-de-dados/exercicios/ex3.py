"""ex03.py   
○ Solicite ao usuário o mês do ano em formato numérico: 1, 2, 3, ..., 12.  
○ Apresente o nome do mês correspondente (ex.: entrada 3 → saída 
Março).  
○ Implementar usando um Dicionário (dict). """

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

mes = int(input("Digite o número do mês (1 a 12): "))

if mes in meses:
    print("Mês:", meses[mes])
else:
    print("Mês inválido")

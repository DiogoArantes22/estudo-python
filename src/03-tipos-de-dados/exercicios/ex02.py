"""ex02.py  
○ Solicite ao usuário o mês do ano em formato numérico: 1, 2, 3, ..., 12.  
○ Apresente o nome do mês correspondente (ex.: entrada 3 → saída 
Março).  
○ Implementar usando uma Tupla (tuple). """

meses = (
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
)

mes = int(input("Digite o número do mês (1 a 12): "))

if 1 <= mes <= 12:
    print("Mês:", meses[mes - 1])
else:
    print("Mês inválido")

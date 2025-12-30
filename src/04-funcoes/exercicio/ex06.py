"""ex06.py: Crie um programa em Python que recebe como entrada o 
comprimento, altura e largura (em cm) de um aquário e calcule: 
○ O volume do aquário em litros;  
○ A potência do termostato necessária para manter a temperatura adequada;  
○ A quantidade de filtragem por hora (em litros) necessária para manter a 
qualidade da água. """


def calcular_volume(aquario):
    #Calculo volume em litros = (C x A x L) / 1000
    comprimento = aquario['comprimento']
    altura = aquario['altura']
    largura = aquario['largura']

    volume = (comprimento * altura * largura) / 1000
    return volume


def calcular_potencia_termostato(volume, temp_desejada, temp_ambiente):
    #calculo potencia em watts = Volume x 0.05 x (Temp_desejada - Temp_ambiente)
    potencia = volume * 0.05 * (temp_desejada - temp_ambiente)
    return potencia


def calcular_filtragem(volume):
    #calculo filtragem em litros por hora = Volume x 2 a 3 vezes
    minimo = volume * 2
    maximo = volume * 3
    return minimo, maximo


# Programa principal
comprimento = float(input("Digite o comprimento do aquário (cm): "))
altura = float(input("Digite a altura do aquário (cm): "))
largura = float(input("Digite a largura do aquário (cm): "))

temp_desejada = float(input("Digite a temperatura desejada (°C): "))
temp_ambiente = float(input("Digite a temperatura ambiente (°C): "))

aquario = {
    'comprimento': comprimento,
    'altura': altura,
    'largura': largura
}

volume = calcular_volume(aquario)
potencia = calcular_potencia_termostato(volume, temp_desejada, temp_ambiente)
filtragem_min, filtragem_max = calcular_filtragem(volume)

print("\nResultados:")
print("Volume do aquário:", round(volume, 2), "litros")
print("Potência do termostato:", round(potencia, 2), "W")
print("Filtragem recomendada por hora:")
print("Mínimo:", round(filtragem_min, 2), "L/h")
print("Máximo:", round(filtragem_max, 2), "L/h")
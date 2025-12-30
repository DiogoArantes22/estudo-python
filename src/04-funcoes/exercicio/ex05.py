"""ex05.py: Implemente uma calculadora de Índice de Massa Corporal (IMC) 
usando as diretrizes da OMS"""


def calcular_imc(individuo):
    # retorna o IMC = peso / (altura * altura)
    peso = individuo['peso']
    altura = individuo['altura']
    imc = peso / (altura * altura)
    return imc


def cassificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


def situacao_individuo(imc):
    if imc < 18.5:
        return "Precisa ganhar peso"
    elif 18.5 <= imc < 24.9:
        return "Manter peso"
    else:
        return "Precisa perder peso"

breakpoint()
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

indiviuo = {
    'peso': peso,
    'altura': altura
}
imc = calcular_imc(indiviuo)
classificacao = cassificar_imc(imc)
situacao = situacao_individuo(imc)

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Situação: {situacao}")

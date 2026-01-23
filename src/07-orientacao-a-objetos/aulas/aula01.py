"""Aula 03- Introdução à Orientação a Objetos em Python."""

# Orientação a Objetos (OO) é um paradigma de programação que utiliza "objetos" para representar dados e funcionalidades.
# Em Python, tudo é um objeto, incluindo tipos de dados primitivos como inteiros e strings.

#Exemplo: Calcular a area e o perimetro de um retangulo sem Orientação a Objetos

#estrutura paea armazenar os valores neccessarios para os calculos 
#area = base * altura
#perimetro = 2 * (base + altura)

retangulo1 = {
    "base": 10.0,
    "altura": 5.0
}

retangulo2 = {
    "base": 6.0,
    "altura": 3.0
}

#Realizar os calculos

def calcular_area(retangulo):
    return retangulo["base"] * retangulo["altura"]

def calcular_perimetro(retangulo):
    return 2 * (retangulo["base"] + retangulo["altura"])

area1 = calcular_area(retangulo1)
perimetro1 = calcular_perimetro(retangulo1)
area2 = calcular_area(retangulo2)
perimetro2 = calcular_perimetro(retangulo2)
print(f"Retângulo 1 - Área: {area1}, Perímetro: {perimetro1}")
print(f"Retângulo 2 - Área: {area2}, Perímetro: {perimetro2}")


#Resolvendo o mesmo problema com Orientação a Objetos

#Classe represnta um conceito ou entidade do mundo real
#Classe Retangulo representa um retangulo com base e altura
#Classe possui atributos (base, altura) e métodos (calcular_area, calcular_perimetro)
class Retangulo:
    #Construtor - método especial para inicializar objetos
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

#Instanciação - criação de objetos a partir de uma classe
retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)
retangulo3 = Retangulo(5.0, 2.5)

print(type(retangulo1),retangulo1)
print(type(retangulo2),retangulo2)

print(retangulo1.base,retangulo1.altura, retangulo1.calcular_area(), retangulo1.calcular_perimetro())
print(retangulo2.base,retangulo2.altura, retangulo2.calcular_area(), retangulo2.calcular_perimetro())
print(retangulo3.base,retangulo3.altura, retangulo3.calcular_area(), retangulo3.calcular_perimetro())
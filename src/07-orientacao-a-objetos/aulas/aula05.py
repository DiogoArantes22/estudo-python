"""Aula 05 -  Metodos especiais em Python."""

# Métodos especiais, também conhecidos como "dunder methods" (double underscore), são métodos predefinidos em Python que permitem personalizar o comportamento de classes e objetos.
# Eles são identificados por nomes que começam e terminam com dois sublinhados (__).

#__str__(self): Define a representação em string de um objeto, usada por funções como print() e str().
#__repr__(self): Fornece uma representação oficial do objeto, usada principalmente para depuração.
#logging, debugging 
#representação canônica do objeto

class Retangulo:
   
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
   
        
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f'Retângulo[base={self.base}, altura={self.altura}]'
    
    def __repr__(self):
        return f'Retangulo(base={self.base}, altura={self.altura})'
    
retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(3.0, 14.0)

retangulo3 = eval('Retangulo(7.5, 12.3)')  #Usando eval para criar um objeto a partir da representação string fornecida por __repr__()

retangulo4 = eval(repr(retangulo3))  #Usando eval para criar um objeto a partir da representação string fornecida por __repr__()
print(retangulo1)  #Chama o método __str__()
print(retangulo2)  #Chama o método __str__()
print(retangulo3)  #Chama o método __str__()
print(retangulo4)  #Chama o método __str__()
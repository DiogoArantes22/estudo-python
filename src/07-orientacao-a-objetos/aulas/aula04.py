"""Aula 04 - Propriedades em Python."""

#Propriedades é uma forma de controlar o acesso aos atributos de uma classe, permitindo a implementação de lógica adicional ao obter ou definir valores.
#Usando o decorador @property, podemos definir métodos que agem como atributos, permitindo encapsulamento e validação de dados.

class Retangulo:
   
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    #property para o atributo base para adicionar validação ao definir o valor
    #getter
    @property
    def base(self):
        return self._base
    
    #setter
    @base.setter
    def base(self, valor):
        if valor <= 0.0:
            raise ValueError("A base deve ser um valor positivo.")
        self._base = valor
        
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if valor <= 0.0:
            raise ValueError("A altura deve ser um valor positivo.")
        self._altura = valor
        
    #Decorador para definir um método de classe
    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])
    
    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=",")
        return cls(float(base), float(altura))
        
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
retangulo1 = Retangulo(10.0, 5.0)
retangulo1.base = 30.0 #Modificando diretamente o atributo base/ problema: pode deixar valores inválidos



print(retangulo1.base)

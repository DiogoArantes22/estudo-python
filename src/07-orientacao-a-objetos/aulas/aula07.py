"""Aula 07 - Relacionamento entre classes em Python.
"""

#Relacionamento entre classes é um conceito fundamental na programação orientada a objetos, onde uma classe pode interagir com outra classe de várias maneiras, como associação, agregação e composição.
#Exemplo de Associação: Uma classe "Aluno" e uma classe "Curso". Um aluno pode estar inscrito em vários cursos, e um curso pode ter vários alunos inscritos.

class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero
        
    def __str__(self):
        return f'Endereço(CEP={self.cep}, Número={self.numero})'

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero
        
    def __str__(self):
        return f'Telefone({self.ddd}) {self.numero}'

class Pessoa:
    def __init__(self, cpf, nome, telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = []  #Lista para armazenar múltiplos endereços (Agregação)
        
    def adicionar_endereco(self, endereco):
        self.enderecos.append(endereco)
        
    def print_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(endereco)
        
    def __str__(self):
        return f'Pessoa[CPF={self.cpf}, Nome={self.nome}, Telefone={self.telefone}]'
    
telefone = Telefone("11","99999-9999")  
pessoa1 = Pessoa("100100100-11","Diogo",telefone)
pessoa1.adicionar_endereco(Endereco("12345-678",100))
pessoa1.adicionar_endereco(Endereco("12345-232",103))

pessoa2 = Pessoa("200200200-22","Maria",telefone)
pessoa2.adicionar_endereco(Endereco("98765-432",200))
print(pessoa1)
print(pessoa1.telefone.ddd, pessoa1.telefone.numero)

print(pessoa2)

pessoa1.print_enderecos()
pessoa2.print_enderecos()
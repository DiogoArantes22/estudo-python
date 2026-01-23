"""Aula 06 - equal e hash code em Python."""
# Métodos __eq__ e __hash__ são usados para definir como os objetos de uma classe são comparados por igualdade e como eles são armazenados em estruturas de dados baseadas em hash, como dicionários e conjuntos.

nome1 = "Diogo"
nome2 = "Diogo"

print(nome1 == nome2)  #True, pois compara o valor das strings

class Pessoa:
    
    def __init__(self,cpf, nome):
        self.cpf = cpf
        self.nome = nome
        
    def __eq__(self, value):
        #instance verifica se o objeto é uma instância da classe Pessoa
        if isinstance(value, Pessoa):
            return self.cpf == value.cpf
        return False
    
    def __hash__(self):
        return hash(self.cpf)
    
    def __repr__(self):
        return f'Pessoa({self.cpf},{self.nome})'
        
        
pessoa1 = Pessoa("100100100-11","Diogo")
pessoa2 = Pessoa("100100100-11","Diogo")
pessoa3 = Pessoa("100100100-10","Maria")

pessoas = {pessoa1,pessoa2, pessoa3}  #Usando o método __hash__ para armazenar objetos em um conjunto
print(pessoas)  #Mostra que pessoa1 e pessoa2 são considerados iguais e armazenados como um único objeto no conjunto
print(pessoa1 == pessoa2)  #True, pois compara o CPF dos objetos


pessoas_lista = [pessoa1, pessoa2, pessoa3]
print(pessoas_lista)

print(pessoas_lista.count(pessoa1))
"""Aula 8 -  Herança entre classes em Python."""
#Herança é um princípio fundamental da programação orientada a objetos que permite criar uma nova classe baseada em uma classe existente.
#A classe derivada (subclasse) herda atributos e métodos da classe base (superclasse), permitindo reutilização de código e criação de hierarquias de classes.

#Exemplo: Classe Pessoa como superclasse e Classe Cliente como subclasse que herda de Pessoa
class Pessoa: #Superclasse
    def __init__(self, nome, sobrenome, cpf):  #4
        print("Entrei no construtor da classe Pessoa")  #5
        self.nome = nome  #6
        self.sobrenome = sobrenome  #7
        self.cpf = cpf  #8
        
    def obtem_nome_completo(self):  #11
        return f'{self.nome} {self.sobrenome}'  #12
    
class Cliente(Pessoa):#Cliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf):  #2
        super().__init__(nome, sobrenome, cpf)   #3 #Chama o construtor da superclasse Pessoa
        self.compras = []   #9  #Atributo específico da classe Cliente
        
"""Exercicio: Crie uma classe chamada funcionario que herda as informações da classe pessoa"""

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario
        
    def calcula_pagamento(self):
        return self.salario - ((10/100) * self.salario)  #Exemplo simples de desconto de 10% no salário
        
        
class Programador(Funcionario):
    def __init__(self,nome,sonbrenome,cpf,salario,bonus):
        super().__init__(nome,sonbrenome,cpf,salario)
        self.bonus = bonus
        
    def calcula_pagamento(self):
        pagamento_salario = super().calcula_pagamento()
        return pagamento_salario + self.bonus

cliente1 = Cliente ('Diogo', 'Arantes', '100100100-11')  #1
print(cliente1.obtem_nome_completo())  #10
print(type(cliente1))  #13

funcionario1 = Funcionario('Maria', 'Silva', '200200200-22', 5000.0)
print(funcionario1.obtem_nome_completo())
print(funcionario1.calcula_pagamento())

programador1 = Programador('João', 'Silva', '300300300-33', 5000.0, 200.0)
print(programador1.obtem_nome_completo())
print(programador1.calcula_pagamento())




    # class Cliente: 
    #     def __init__(self,nome, sobrenome, cpf):
    #         self.nome = nome
    #         self.sobrenome = sobrenome
    #         self.cpf = cpf
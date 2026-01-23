"""Aula 02-  Atributos de classe e instância em Python."""

#classe pessoa possui atributos de instância nome e email
class Pessoa:
    
    especie = 'Humano'  #atributo de classe compartilhado por todas as instâncias
    
    
    
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        


pessoa1 = Pessoa('Diogo Arantes', 'diogoarantes@gmail.com')
pessoa2 = Pessoa('Maria Silva', 'maria@email.com')

print(pessoa1.nome, pessoa1.email)
print(pessoa2.nome, pessoa2.email)


#Alterar um atributo de calasse na instacia altera somente para aquela instância
pessoa1.especie = 'Alienígena'  #Cria um atributo de instância com o mesmo nome do atributo de classe
print(Pessoa.especie)  #Acessando atributo de classe via classe
print(pessoa1.especie)  #Acessando atributo de classe via instância


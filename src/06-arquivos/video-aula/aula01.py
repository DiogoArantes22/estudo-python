"""Aula 01 - Manipulação de Arquivos em Python"""

# open() - abre um arquivo,rece dois parâmetros: nome do arquivo e modo de abertura
# modos de abertura:
# 'r' - leitura (padrão)
# 'w' - escrita (sobrescreve o arquivo)
# 'a' - escrita (adiciona ao final do arquivo)
# x - criação (cria o arquivo, se já existir, gera erro)
# 'b' - modo binário
# r+ - leitura e escrita


# 1 passo - abrir o arquivo, open() retorna um objeto do tipo file, utilze uma variável para armazenar esse objeto
# aula01.py

# arquivo = open("text2.txt", "w")  # abre o arquivo em modo de leitura


# # print(arquivo.readable()) # verifica se o arquivo está em modo de leitura

# # print(arquivo.read()) # lê o conteúdo do arquivo

# # lê o conteúdo do arquivo e retorna uma lista com as linhas do arquivo
# # print(arquivo.readline())
# # print(arquivo.readline())
# # print(arquivo.readline())
# # print(arquivo.readline())

# # lê o conteúdo do arquivo e retorna uma lista com as linhas do arquivo
# # lista = arquivo.readlines()

# # print(lista)

# # print(lista[0])  # acessa a primeira linha da lista



# #Fazendo o appêndice em um arquivo, que é adicionar conteúdo ao final do arquivo
# # arquivo = open("text.txt", "a")  # abre o arquivo em modo de

# # escrita (adiciona ao final do arquivo)
# # arquivo.write("\nPython")  # adiciona uma nova linha com o texto "Python" ao final do arquivo

# #diferenca entre abrir em modo 'w' e 'a'
# # 'w' - sobrescreve o arquivo e também cria o arquivo se ele não existir
# # 'a' - adiciona ao final do arquivo
# # arquivo.write("Pyton\n")
# # arquivo.write("TypeS\n")
# # arquivo.write("Terraform\n")



# arquivo.close()  # fecha o arquivo

#remover um arquivo dentro de uma pasta
#import os é a biblioteca responsável por interagir com o sistema operacional
import os 

# os.remove("text3.txt")  # remove o arquivo text3.txt

# if os.path.exists("text2.txt"):  # verifica se o arquivo existe
#     os.remove("text2.txt")  # remove o arquivo text3.txt
# else:
#     print("O arquivo não existe")

#deltar pasta
# os.rmdir("pasta_teste")  # remove a pasta pasta_teste (a pasta deve estar vazia)

# os.rmdir("src/06-arquivos/nova_pasta")  # remove a pasta nova-pasta (a pasta deve estar vazia)
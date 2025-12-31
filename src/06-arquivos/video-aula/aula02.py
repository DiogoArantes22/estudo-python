"""Dominar manipulação de arquivos em Python é essencial para diversas aplicações, desde o armazenamento de dados até a configuração de sistemas."""

# Criando e escrevendo em um arquivo
# arq = open('arquivo.txt', 'w')

# # string = 'Ola diogo tudo bem?\n'

# # lista = ['Olá', 'Diogo', 'tudo', 'bem?']

# # diferentes formas de escrever em um arquivo
# # write - escreve uma string no arquivo
# # writelines - escreve uma lista no arquivo
# # arq.writelines()

# # arq.write('Ola diogo tudo bem?\n')

# x = ['caio\n', 'joao\n', 'maria\n']
# # arq.writelines(x)

# for nome in x:
#     arq.write(nome )
# arq.close()


# Abrindo arquivo texto com o gerenciador de contexto (with)

# with open('arquivo.txt', 'a') as arq:
#   arq.write('\ncaiota')

# print('Arquivo escrito com sucesso!')

with open('arquivo.txt', 'r') as arq:
    
    x = arq.read( )
    print(x)
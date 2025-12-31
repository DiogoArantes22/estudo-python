"""ex01.py – Carregar dados de alunos. Implemente a função: carregar_dados_alunos(nome_arquivo) que recebe o nome de um arquivo texto como parâmetro. O arquivo contém informações de alunos, onde cada linha possui o formato: nome,idade,curso. A função deve ler o arquivo e retornar uma tupla de dicionários, onde cada dicionário representa um aluno com as chaves 'prontuario', 'nome' e 'email'.

Exemplo de arquivo de dados (texto): 
SP000001,Maria da Silva,maria@email.com 
SP000002,Pedro Gomes,pedro@email.com 
SP000003,João Santos,joao@email.com

Desenvolver a logica de leitura e processamento "na mãop"a, sem usar bibliotecas externas para manipulação de arquivos.

Implementar a separação dos campos a partir da string da linha
"""
def carregar_dados_alunos(nome_arquivo):
    alunos = [] 
    
    with open(nome_arquivo,'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            dados = linha.split(',')
            
            aluno = {
                'prontuario': dados[0],
                'nome': dados[1],
                'email': dados[2]
            }
            
            alunos.append(aluno)
            
        return tuple(alunos)
        
        
resultado = carregar_dados_alunos('src/06-arquivos/exercicios/alunos.txt')

for aluno in resultado:
    print(f'{aluno['prontuario']} | {aluno['nome']} | {aluno['email']}')
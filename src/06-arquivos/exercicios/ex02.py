"""Ex02- Carregar dados de projetos. Implemente a função: 
def carregar_dados_projetos(nome_arquivo): 

 Carregar dados de projetos. Implemente a função: 
def carregar_dados_projetos(nome_arquivo): 
Retorna uma tupla de dicionários com dados de 
projetos.

"""

def carregar_dados_projetos(nome_arquivo):
    
    projetos = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            dados = linha.split(',')
            
            projeto = {
                'codigo': int(dados[0]),
                'titulo': dados[1],
                'responsavel': dados[2]
            }
            
            projetos.append(projeto)
            
        return tuple(projetos)
    
    
    
resultado = carregar_dados_projetos('src/06-arquivos/exercicios/projetos.txt')
    
for linha in resultado:
    print(f'{linha['codigo']} | {linha['titulo']} | {linha['responsavel']}')
            
        
"""Ex 3- Convertendo uma linha em dicionário genérico.  """

def linha_para_dict(linha, chaves):
    linha = linha.strip()
    valores = linha.split(",")

    dicionario = {}

    for i in range(len(chaves)):
        dicionario[chaves[i]] = valores[i]

    return dicionario


# testes
linha1 = 'SP000001,Maria da Silva,maria@email.com'
chaves1 = ['prontuario', 'nome', 'email']
print(linha_para_dict(linha1, chaves1))

linha2 = 'banana,3'
chaves2 = ['item', 'quantidade']
print(linha_para_dict(linha2, chaves2))
    
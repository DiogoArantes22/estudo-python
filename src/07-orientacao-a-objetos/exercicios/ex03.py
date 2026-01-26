"""Ex02 - Classe Participação"""

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    def __str__(self):
        return (
            f"Participação {self.codigo}\n"
            f"Aluno: {self.aluno.nome}\n"
            f"Projeto: {self.projeto.titulo}\n"
            f"Início: {self.data_inicio} | Fim: {self.data_fim}"
        )

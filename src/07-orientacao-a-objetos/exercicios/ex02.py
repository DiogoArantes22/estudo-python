"""Ex02 - Classe Projeto"""

class Projeto:
    def __init__(self, dados):
        codigo, titulo, responsavel = dados.split(',')

        self.codigo = int(codigo.strip())
        self.titulo = titulo.strip()
        self.responsavel = responsavel.strip()
        self.participacoes = []

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None:
            raise ValueError("Código não pode ser nulo.")
        self._codigo = valor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError("Título não pode ser vazio.")
        self._titulo = valor

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if not valor:
            raise ValueError("Responsável não pode ser vazio.")
        self._responsavel = valor

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)

    def __eq__(self, other):
        if not isinstance(other, Projeto):
            return False
        return self.codigo == other.codigo

    def __str__(self):
        return f"Projeto {self.codigo} - {self.titulo} ({self.responsavel})"

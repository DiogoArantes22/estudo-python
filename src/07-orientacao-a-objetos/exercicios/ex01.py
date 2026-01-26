"""Ex01 - Classe Aluno """

class Aluno:
    def __init__(self, dados):
        prontuario, nome, email = dados.split(',')

        self.prontuario = prontuario.strip()
        self.nome = nome.strip()
        self.email = email.strip()

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor):
        if not valor:
            raise ValueError("Prontuário não pode ser vazio.")
        self._prontuario = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio.")
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor:
            raise ValueError("Email não pode ser vazio.")
        self._email = valor

    def __eq__(self, other):
        if not isinstance(other, Aluno):
            return False
        return self.prontuario == other.prontuario

    def __hash__(self):
        return hash(self.prontuario)

    def __str__(self):
        return f"{self.prontuario} - {self.nome} ({self.email})"

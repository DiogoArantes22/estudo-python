"""Ex04 - Lista de participações no projeto"""

from ex01 import Aluno
from ex02 import Projeto
from ex03 import Participacao

aluno1 = Aluno("SP0001,Diogo Arantes Borges,diogo@gmail.com")
aluno2 = Aluno("SP0002,Pedro Gomes,pedro@gmail.com")

projeto = Projeto("1,LIPAI,Prof. Marcelo")
projeto2 = Projeto("2,Visão Computacional,Prof. Glaucia")

participacao1 = Participacao(1, "2026-03-01", "2026-06-30", aluno1, projeto)
participacao2 = Participacao(2, "2026-04-01", "2026-07-30", aluno2, projeto)

projeto.add_participacao(participacao1)
projeto.add_participacao(participacao2)
print(projeto)
print("\nParticipações:")
for p in projeto.participacoes:
    print("------------------")
    print(p)

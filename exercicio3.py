# Crie uma classe Aluno com atributos como nome, idade e nota. Em seguida, crie uma classe Turma
# que armazena vários alunos e possui métodos para adicionar aluno, calcular média das notas e listar alunos.

class Aluno:
    def __init__(self, nome, idade, nota):
        self._nome = nome
        self._idade = idade
        self._nota = nota

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nova_nota):
        self._nota = nova_nota


class Turma:
    def __init__(self):
        self.lista_alunos = []

    def __len__(self):
        return len(self.lista_alunos)

    def adiciona_aluno(self, novo_aluno):
        self.lista_alunos.append(novo_aluno)

    def calcula_media(self):
        total_notas = sum(aluno._nota for aluno in self.lista_alunos)
        media = total_notas / len(self.lista_alunos)
        return media

    def imprime_alunos(self):
        for aluno in self.lista_alunos:
            print(aluno._nome)


# teste das funcionalidades:
turma = Turma()

aluno1 = Aluno('Pedro', 14, 8.5)
aluno2 = Aluno('Jonas', 13, 4)
aluno3 = Aluno('Carla', 14, 6.1)
aluno4 = Aluno('Maria', 15, 10)

aluno2.nome = 'Jonar'

turma.adiciona_aluno(aluno1)
turma.adiciona_aluno(aluno2)
turma.adiciona_aluno(aluno3)
turma.adiciona_aluno(aluno4)

turma.imprime_alunos()
turma.calcula_media()
print(turma.calcula_media())

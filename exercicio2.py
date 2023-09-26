# Crie uma classe Contato para representar informa¸c˜oes de contato, como nome, telefone e e-mail. Em
# seguida, crie uma classe Agenda que armazena vérios contatos e possui métodos para adicionar, remover e listar
# contatos.

class Contato:
    def __init__(self, nome, telefone, email):
        super().__init__()
        self._nome = nome
        self._telefone = telefone
        self._email = email

    def __str__(self):
        return f'Nome: {self._nome}\t\tTelefone: {self._telefone}\t\tE-mail: {self._email}.'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email


class Agenda:
    def __init__(self):
        self.lista_contatos = []

    def __len__(self):
        return len(self.lista_contatos)

    def total_contatos(self):
        print(f'Sua agenda tem o total de {len(self.lista_contatos)} contados')

    def adiciona_contato(self, nome_contato):
        self.lista_contatos.append(nome_contato)

    def remove_contato(self, indice_contato):
        self.lista_contatos.pop(int(indice_contato))

    def imprime(self):
        for contato in self.lista_contatos:
            print(f'INDICE: {self.lista_contatos.index(contato)}\tNome: {contato._nome}\t\t'
                  f'Telefone: {contato._telefone}\t\tE-mial: {contato._email}\n')


# teste das funcionalidades:
agenda = Agenda()

contato1 = Contato('Lucas', '(21)2444-5667', '123@gmail.com')
contato2 = Contato('Joana', '(22)3465-8900', '124@gmail.com')
contato3 = Contato('Pedro', '(21)993457832', '322@gmail.com')
contato4 = Contato('Caio', '(11)987564312', '327@gmail.com')

contato1.nome = 'Otávio'

agenda.adiciona_contato(contato1)
agenda.adiciona_contato(contato2)
agenda.adiciona_contato(contato3)
agenda.adiciona_contato(contato4)

agenda.remove_contato(2)

agenda.imprime()

agenda.total_contatos()

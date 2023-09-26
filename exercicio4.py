# Crie uma classe Produto para representar itens de uma loja, com atributos como nome, preço e
# quantidade em estoque. Crie uma classe Carrinho que permite adicionar produtos, calcular o total e finalizar a
# compra.

class Produto:
    def __init__(self, nome, preco, estoque):
        self._nome = nome
        self._preco = preco
        self._estoque = estoque

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco

    def get_estoque(self):
        pass

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, nova_qnt):
        self._estoque = nova_qnt
class Carrinho:
    def __init__(self):
        self.carrinho = []

    def adiciona_produto(self, produto):
        self.carrinho.append(produto)

    def imprime_produtos(self):
        for produto in self.carrinho:
            print(f'Porduto: {produto._nome}\t/ Preço: {produto._preco}')

    def calcula_total(self):
        total = sum(produto._preco for produto in self.carrinho)
        print(f'Total Carrinho: R${total}')

    def finaliza_compra(self):
        print(f'Compra finalizada')
        self.carrinho.clear()


# teste das funcionalidades:
carrinho = Carrinho()

produto1 = Produto('Microfone HyperX QuadCast', 900, 3)
produto1.preco = 3000
produto1.estoque = 20

produto2 = Produto('Teclado Mecânico X', 350, 1)
produto3 = Produto('Iphone 14 Pro', 6299, 2)

carrinho.adiciona_produto(produto1)
carrinho.adiciona_produto(produto2)
carrinho.adiciona_produto(produto3)

carrinho.imprime_produtos()
carrinho.calcula_total()
carrinho.finaliza_compra()

carrinho.calcula_total()

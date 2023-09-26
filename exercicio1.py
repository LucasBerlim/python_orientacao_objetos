# Crie uma classe ContaBancaria com métodos para depositar, sacar e consultar saldo. Crie uma instância da
# classe e teste suas funcionalidades.

class ContaBancaria:
    def __init__(self, numero_conta, nome, saldo):
        self.__numero_conta = numero_conta
        self.__nome = nome.title()
        self.__saldo = saldo

    def saca(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo = self.__saldo - valor
        else:
            print('Saldo insuficiente.')

    def deposita(self, valor):
        if valor > 0:
            self.__saldo = self.__saldo + valor
        else:
            print('O valor precisa ser maior que zero.')

    def get_saldo(self):
        print(f'Seu saldo é {self.__saldo}')


# teste das funcionalidades:
conta1 = ContaBancaria(123, 'Lucas', 1400)

conta1.get_saldo()
conta1.saca(200)
conta1.get_saldo()
conta1.deposita(5000)
conta1.get_saldo()
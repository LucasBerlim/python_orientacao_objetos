# Crie uma classe JogoAdivinhacao que representa um jogo simples de adivinhação. A classe deve
# gerar um número aleatório entre 1 e 100 e permitir que o jogador fa¸ca várias tentativas para adivinhar o
# número. A cada tentativa, o jogo deve dar dicas se o número é maior ou menor. Quando o jogador acertar, o
# jogo deve exibir quantas tentativas foram necessárias e perguntar se o jogador deseja jogar novamente. Lembre-se
# de incluir um método construtor para iniciar o jogo, métodos para realizar as tentativas, métodos para dar dicas
# e um método para reiniciar o jogo se o jogador quiser jogar novamente.

import random

class JogoAdivinhacao:
    def __init__(self):
        self.random_number = random.randint(1, 100)
        self.tentativa = 0

    def tenta(self, numero):
        self.tentativa += 1
        if(numero > self.random_number):
            return f'O número que você chutou é maior que o número aleatório'
        elif(numero < self.random_number):
            return f'O número que você chutou é menor que o número aleatório'
        elif(numero == self.random_number):
            return f'Parabéns, você acertou! Tentativas usadas: {self.tentativa}'

    def recomeca_jogo(self):
        self.random_number = random.randint(1, 100)
        self.tentativa = 0


jogo = JogoAdivinhacao()

while True:
    numero = int(input('Chute um número de 1 a 100: '))
    tentativa = jogo.tenta(numero)
    print(tentativa)
    if jogo.random_number == numero:
        print('Deseja jogar novamente?\n1- SIM\n2- NÃO')
        escolha = int(input('Esolha: '))
        if escolha == 1:
            jogo.recomeca_jogo()
        else:
            break

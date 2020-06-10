# Melhore o jogo do desafio 28 em que o computador pensa em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print('Desafio da adivinhação!! Vou pensar em um número de \033[34m1 a 10\033[m e você vai tentar adivinhar.')
from random import randint
n1 = randint(1, 11)
n2 = int(input('Digite seu palpite! '))
tentativas = 1
while n2 != n1:
    n2 = int(input('Tente novamente: '))
    tentativas += 1
print(f'Após {tentativas} tentativas, você acertou! Pensei no {n1}.')

# feito.
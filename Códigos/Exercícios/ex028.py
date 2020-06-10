# Escreva um programa que faça o computador 'pensar' em um número inteiro entre
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
# computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

print('Jogo de adivinhação! Eu vou pensar em um número inteiro de 1 a 5\n'
      'e você vai ter que adivinhar qual é! Vamos?')
from random import randint
n1 = randint(1, 5)
n2 = int(input('Em qual número eu pensei? '))
if n1 == n2:
    print('Você acertou! Era {} mesmo.'.format(n1))
else:
    print('Errado. Eu pensei no {}, e não no {}'.format(n1, n2))
from time import sleep
sleep(3)
print('-=-' * 20)

# Feito ok
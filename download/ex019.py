# 19 sorteio de um dos quatro alunos

aluno1 = input('Digite o nome de um dos alunos ')
aluno2 = input('Agora de outro: ')
aluno3 = input('Mais um: ')
aluno4 = input('O último: ')
from random import randint

numero = randint(1, 4)
if numero == 1:
    sorteado = aluno1
if numero == 2:
    sorteado = aluno2
if numero == 3:
    sorteado = aluno3
if numero == 4:
    sorteado = aluno4

print('Aguarde... estamos sorteando...')
print('O escolhido foi', sorteado)

# print('O escolhido foi {}!'.format(if numero == 1: aluno1, if numero == 2: aluno2)) nada a ver
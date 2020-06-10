# quatro jogadores jogam um dado, guardar os resultados em um dicionário.
# colocar o dicionário em ordem, sabendo que o vencedor tirou o maior número no dado
# não tem input, usar sleep

from random import randint
from time import sleep
from operator import itemgetter
jogos = dict()
for j in range(1, 5):
    jogos[f'Jogador{j}'] = randint(1, 6)
for k, v in jogos.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)
print('=-' * 20)
print(f"{'== RANKING DOS JOGADORES ==':^30}")

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('=-' * 20)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} = {v[1]}')
    sleep(0.5)

# Ok
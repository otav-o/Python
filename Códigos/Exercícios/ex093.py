# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


def s(n):
    """Use isso para Separar as informações exibidas ao usuário
    :return: none"""
    print('=-' * n)


gols = list()
jogador = dict()
jogador['nome'] = input('Nome: ')
num = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
totgols = 0     # não precisava. Existe o sum(lista).
for p in range(1, num + 1):
    g = int(input(f'Quantos gols na partida {p}? '))
    gols.append(g)
    totgols += g
jogador['gols'] = gols
jogador['total'] = totgols[:]
s(20)
print(jogador)
s(20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
s(25)
print(f'O jogador {jogador["nome"]} jogou {num} partidas.')     # num == len(jogador['gols']
for i, v in enumerate(gols):
    print(f'==> Na partida {i + 1}, fez {v} gols')
print(f'Foi um total de {totgols} gols.')       # totgols == jogador['total']

# Feito. Ok

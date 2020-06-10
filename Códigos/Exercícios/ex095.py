# Aprimoramento do ex093: vários jogadores + sistema de visualização
jogadores = list()
jogador = {}
gols = []
while True:
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, partidas + 1):
        gols.append(int(input(f'    Quantos gols na partida {p}? ')))
    jogador['gols'] = gols[:]   # copia a lista de gols para o dicionário
    jogador['total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())    # adiciona uma cópia do dict. jogador para a lista jogadores
    while True:
        perg = input('Quer continuar? ').strip().upper()[0]
        if perg in 'SN':
            break
        print('Comando inválido! Digite sim ou não')
    if perg == 'N':
        break
print(jogadores)
print('=-' * 20)
print(f"{'cod':>4}", end='')
print(f'{" nome":<15}', end='')
print(f'{"gols":<15}', end='')
print('total')
print('-' * 40)
for d in range(0, len(jogadores)):      # lista
    print(f'{d:>4}', end='')
    print(f' {jogadores[d]["nome"]:<14}', end='')
    print(f'{str(jogadores[d]["gols"]):<15}', end='')   # só existe manipulação de texto com string
    print(f'{jogadores[d]["total"]}')
print('-' * 60)
while True:
    resp = int(input('Quer ver os gols de qual jogador? [999 para parar] '))
    if resp == 999:
        break
    elif resp not in range(0, len(jogadores)):
        print(f'Nenhum jogador possui o código {resp}! Tente de novo.')
    else:
        for i, v in enumerate(jogadores[resp]['gols']):
            print(f'Na partida {i + 1}, {jogadores[resp]["nome"]} fez {v} gols')
        print(f'{jogadores[resp]["nome"]} fez {jogadores[resp]["gols"]} gols.')
print('FIM DO PROGRAMA')


# Ok. Feito
# 18/05/2020
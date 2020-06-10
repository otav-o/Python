'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasieiro de Futebol, na ordem de
colocação. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os úlimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética
d) Em que posição na tabela está o time da Chapecoense.'''

a = ('Corinthians',	'Palmeiras', 'Santos', 'Grêmio',
     'Cruzeiro', 'Flamengo',	'Vasco da Gama', 'Chapecoense',
     'Atlético-MG',	'Botafogo',	'Athletico-PR', 'Bahia',
     'São Paulo', 'Fluminense', 'Sport', 'Vitória',
     'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('=-' * 20)
print('{:^40}'.format('BRASILEIRÃO 2017'))
print('=-' * 20)
resp = input('Você quer ver a classificação dos primeiros ou últimos times da tabela? ').upper().strip()[1]
while resp not in 'RL':
    resp = input('Comando inválido. Digite "primeiros" ou "últimos". ').upper().strip()[1]

n = 0
while n not in range(1, 21):
    n = int(input('Quantos? '))

if resp == 'L':
    times = a[-n:]  # ótimo a[-4:]
elif resp == 'R':
    times = a[:n]   # certo

print(f'Os {n} {"primeiros" if resp == "R" else "últimos"} times são {times}.')
print(f'O time da Chapecoense está na {a.index("Chapecoense") + 1}ª posição.')  # cuidado!
print(f'Os times em ordem alfabética são: {sorted(a)}')

# Feito
# Ok
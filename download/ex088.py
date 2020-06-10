# Palpites para mega-sena; sortear quantos jogos o usuário pedir com o cuidado de não repetir números

from random import randint
print('-' * 30)
print(f'{"MEGA SENA PALPITES":^30}')
print('-' * 30)
n_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
jogo = [[]]

for c in range(1, n_jogos + 1):
    jogo.append([])
    while len(jogo[c]) < 6:
        jogo[c].append(randint(1, 60))
        for num in jogo[c]:
            while jogo[c].count(num) > 1:
                jogo[c].remove(num)
    jogo[c].sort()
    print(f'Jogo {c}: {jogo[c]}')

# Feito. Ok OBS.: nada a ver com a resposta do professor, recomendo vê-la na íntegra


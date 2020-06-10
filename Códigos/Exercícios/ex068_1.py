''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)     # randint inclui o último número
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':     # não permite resposta inválida
        tipo = str(input('Par ou ímpar? ')).upper().strip()
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        elif total % 2 != 0:
            print('Você perdeu!')
            break
    if tipo == 'I':
        print('Você perdeu!') if total % 2 == 0 else print('Você ganhou!')
        if total % 2 != 0:
            v += 1
        else:
            break

print(f'Fim de jogo!! Você venceu {v} vezes consecutivas.')

# ok

# Faça com que o computador jogue pedra, papel, tesoura com você.
a = input('Pedra, papel ou tesoura? ').upper()
from random import randint

if a == 'PEDRA':
    b = 1
elif a == 'PAPEL':
    b = 2
elif a == 'TESOURA':
    b = 3
else:
    b = 0
    print('Reinicie o programa')
c = randint(1, 3)   # ou (0, 2)
if b == c:
    print('Empate! Nós dois escolhemos {}'.format(a))
elif b == 1 and c == 2:   # legenda: 1 - pedra; 2 - papel; 3 - tesoura
    print('Ganhei! Escolhi PAPEL e você PEDRA.')
elif b == 1 and c == 3:
    print('Perdi! Escolhi TESOURA e você PEDRA. Parabéns.')
elif b == 2 and c == 1:
    print('Perdi! Escolhi PEDRA e você PAPEL. Parabéns.')
elif b == 2 and c == 3:
    print('Ganhei! Escolhi TESOURA e você PAPEL.')
elif b == 3 and c == 1:
    print('Ganhei! Escolhi PEDRA e você TESOURA.')
elif b == 3 and c == 2:
    print('Perdi! Escolhi PAPEL e você TESOURA.')

# funciona

# Jeito do professor:  ##############################################

from random import randint
tipos = ('Pedra', 'Papel', 'Tesoura')   # lembrar das aspas
computador = randint(0, 2)

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua escolha? '))
from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-=' * 11)
print('O computador jogou {}'.format(tipos[computador]))
print('Jogador jogou {}'.format(tipos[jogador]))
print('-=' * 11)

if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida.')
elif computador == 1:   # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida.')

elif computador == 2:   # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida.')

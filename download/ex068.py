# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
perg = 'oi'
resp = 0

while perg[0] != 'P' and 'I' and 'Í':   # não funciona!! nem o /and/ nem o /or/
        perg = input('PAR ou ÍMPAR? ').strip().upper()
num = int(input('Jogue seu número: '))
while num > 10: #and num < 0:
    num = int(input('Seu dedo não consegue representar isso. Digite de novo. ' ))
n = randint(0, 11)
if (num + n) % 2 == 0:
    resp = 'PAR'
elif (num + n) % 2 != 0:
    resp = 'ÍMPAR'
if perg == resp:
    resultado = 'ganhou!'
else:
    resultado = 'perdeu.'
print(f'Joguei o número {n}, que somado a {num} dá {n + num} ({resp}). Você {resultado}.')

# ver solução
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles,
# desconsiderando o flag.

s = 0
n = 0
q = 0
while n != 999:
    n = int(input('Digite um número!! [Para interromper: 999] '))
    if n != 999:
        s += n
        q += 1

print('Você digitou {} números, e a soma deles é {}'.format(q, s))

# Feito.
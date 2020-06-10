'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles,
desconsiderando o flag.'''

q = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    q += 1
    s += n

print(f'Você digitou {q} números e a soma entre eles é {s}')

# Feito.
# ok






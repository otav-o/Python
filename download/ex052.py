# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
for q in range(2, n):
    if n % q != 0:
        print('{} é um número primo!'.format(n))
    else:
        print('{} \033[31mnão\033[m é um número primo.'.format(n))

# ficou ruim

núm = int(input('Digite um valor: '))
tot = 0


for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[34m', end= '')  # inicia cor
        tot = tot + 1
    else:
        print('\033[31m', end= '')  # inicia cor
    print(c, end=' ')

if tot == 2:
    resp = 'É PRIMO'
else:
    resp = 'NÃO É PRIMO'

print('\n\033[mO número {} foi divisível {} vezes!!'.format(núm, tot))
print('Logo, ele {}.'.format(resp))

# ok, mas continua estranho
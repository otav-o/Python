# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão: '))
print('Os 10 primeiros termos dessa progressão são: ')
print('Termo 1° = {}'.format(a1))
for n in range(2, 11):
        print('Termo {}° = {}'.format(n, a1 + r * (n -1)))
# feito

# melhorando

print('=' * 30)
print('{:^30}'.format('10 termos de uma PA'))
print('=' * 30)
ai = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
for c in range(1, 11):
    print(ai + ra * (c - 1), end=' -> ')    # ai e ra não mudam de valor, somente o c.
print('ACABOU')

# Ótimo

# Forma feita pelo professor:

primeiro = int(input('Primiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' ~ ')
print('FIM')

# o jeito do professor faz o range saltar pela razão até o último termo da P.A
# ok

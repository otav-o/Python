# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# # a estrutura while

print('x=' * 20)
print('{:^40}'.format('Calculadora de PA'))
print('x=' * 20)

a1 = int(input('Insira o primeiro termo: '))
r = int(input('Digite a razão: '))
n = int(input('Quantos termos você quer mostrar? '))

an = a1 + (n - 1) * r

c = 1
while c <= n:
    termo = a1 + (c - 1) * r
    if c < n:
        print(termo, end=', ')
    elif c == n:
        print(termo, end='.')
    c += 1

# Feito.

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = str(input('Digite um número de zero a 9999: '))

if len(numero) == 4:
    u = numero[3]
    d = numero[2]
    c = numero[1]
    m = numero[0]

if len(numero) == 3:
    u = numero[2]
    d = numero[1]
    c = numero[0]
    m = 0

if len(numero) == 2:
    u = numero[1]
    d = numero[0]
    c = 0
    m = 0

if len(numero) == 1:
    u = numero[0]
    d = 0
    c = 0
    m = 0

print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {} '''. format(u, d, c, m))

# Feito. Mas ficou gigante.

# Tentando fazer certo

n = int(input('Informe um número: '))
un = n // 1 % 10
de = (n // 1 % 100)#[0]
ce = str(n // 1 % 1000)[0]
mi = str(n // 1 % 10000)[0]


print('Unidade: {}'.format(un))
print('Dezena: {}'.format(str(de)[0]))
print('Centena: {}'.format(ce))
print('Milhar: {}'.format(mi))


# fiz por string. Tem como fazer pela matemática:

n1 = int(input('Escreva só mais um número: '))
un1 = n1 // 1 % 10
de1 = n1 // 10 % 10
ce1 = n1 // 100 % 10
mi1 = n1 // 1000 % 10
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(un1, de1, ce1, mi1))

# F E I T O
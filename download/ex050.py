# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado foi ímpar, desconsidere-o.

s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n
print('O somatório dos números pares que você digitou é {}.'.format(s))

# funciona. Mas eu gostaria que fosse menos decorado.
# venho do futuro dizer que isso não é decorado!

# semelhante à tabuada:
z = 0
for b in range(1, 7):   # cuidado: começa no valor zero e termina no 5 (mantendo 6 números). O certo é range(1, 7)
    n1 = int(input('Digite o {}° valor: '.format(b)))
    if n1 % 2 == 0:
        z += n1
print('A soma dos pares é {}'.format(z))

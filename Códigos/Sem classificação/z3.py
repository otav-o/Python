nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:+^923}'.format(nome))


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))

s = n1 + n2
p = n1 * n2
d = n1 / n2
di = n1 // n2
ex = n1 ** n2

print('Os números que você escolheu são {} e {}.\nA soma é {}, o produto, {} e a divisão é {:.3f}.'.format(n1, n2, s, p, d), end = ' ')
print('A divisão inteira dá {} e {} elevado a {} é igual a {}.'.format(di, n1, n2, ex))

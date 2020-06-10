# Refaça o desafio 009 (Está em 'Guanabara 5') , mostrando a tabuada de um número que o usuário escolher, só que
# agora usando o laço for.


# Desafio 009 : tabuada de um número inteiro

n4 = int(input('Vamos gerar a tabuada do seguinte número: '))
print('''Aqui está:
{0} * 1 = {0}
{0} * 2 = {1}
{0} * 3 = {2}
{0} * 4 = {3}
{0} * 5 = {4}
{0} * 6 = {5}
{0} * 7 = {6}
{0} * 8 = {7}
{0} * 9 = {8}
{0} * 10 = {9}'''.format(n4*1, n4*2, n4*3, n4*4, n4*5, n4*6, n4*7, n4*8, n4*9, n4*10))

# Refazendo...

n = int(input('Digite um número para gerarmos a tabuada dele. '))
for c in range(1, 11):
    print('{} * {} = {}'.format(n, c, n * c))   # ótimo
print('FIM')

# deu certo!! em muito menos linhas.


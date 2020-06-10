# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# a) qual é o total gasto na compra
# b) quantos produtos custam mais de R$1000
# c) qual é o nome do produto mais barato

print('-=' * 20)
print(f'{"CALCULADORA DE SUPERMERCADO":^40}')
print('-=' * 20)
c = 1
s = mil = menor = 0
n_barato = ' '
perg = ' '
while True:
    nome = input('Nome do {}° produto: '.format(c))
    p = float(input('Preço do {}° produto: '.format(c)))
    s = s + p
    if p > 1000:
        mil += 1
    if c == 1 or p < menor:
        menor = p
        n_barato = nome
    '''if p < menor:    # evitar 2 blocos iguais
        n_barato = nome
        menor = p'''
    perg = ' '
    while perg[0] not in 'SN':
        perg = input('Deseja continuar? ').upper().strip()
    if perg[0] == 'N':
        break
    c += 1
print(f'Foram registrados {c} produtos, cuja soma de preços dá R${s:.2f}. {mil} custa(m) mais de mil reais e o mais barato foi {n_barato}, que custa R${menor:.2f}.')
                                                                # observe
# feito
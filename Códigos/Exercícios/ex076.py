''' Crie um programa que tenha uma tupla única com os nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''


tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila',
         120.32, 'Canetas', 22.3, 'Livro', 34.90)

print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-' * 40)

for n in range(0, len(tupla)):
    if n % 2 == 0:
        print(f'{tupla[n]:.<25}', end='')   # parabéns
    elif n % 2 != 0:
        print(f'{tupla[n]:>6.2f}')

print('-' * 40)

# Poderiam ser usadas duas tuplas
# Ok
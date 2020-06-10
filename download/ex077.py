'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso. vpcê deve mostrar,
para cada palavra, quais são as suas vogais.'''

tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
'mercado', 'programador', 'futuro')

for palavra in tupla:
    vogais = ''
    a = 'a', 'e', 'i', 'o', 'u'
    for letra in a:
        if letra in palavra:
            vogais += letra + ' '
    print(f'A palavra {palavra.upper()} tem as vogais {vogais}')

# Solução do professor:
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:     # cada palavra é uma listagem de letras
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

# Feito.
# Ok
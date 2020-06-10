# Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra 'Santo'.

cidade = input('Qual o nome da sua cidade? ').strip()
if 'Santo' in cidade.capitalize():  # lembre-se de que é uma string
    print('{} tem "Santo" no início do nome!'.format(cidade.capitalize()))
else:
    print('{} não tem "Santo" no início do nome!'.format(cidade.capitalize()))


# Correção: tem que começar com 'Santo', e não ter essa palavra.
# não sei como deu certo

cid = input('Digite o nome de uma cidade: ').lower().strip()
print('Ela começa com Santo?')
print(cid[0:5] == 'santo')

# Feito

# cidade2 = input('Em qual cidade você mora? ')
# if 'Santo' in cidade.capitalize().split()[0]    # nem rodei e já sei que não atende ao exercício.
# if 'Santo' in cidade2.captalize()[0]


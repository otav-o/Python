# Desenvolva um programa que leia nome, idade, sexo de 4 pessoas. No final, mostre:
# - A média de idade do grupo.
# - Qual é nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.
from pip._internal.vcs import git

s = 0
idadevelho = 0
mulheres_novas = 0
hvelho = ''
for c in range(1, 5):
    print('-=-=-=-=-=-=-= {}ª pessoa =-=-=-=-=-=-='.format(c))
    nome = input('Digite um nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper().strip()
    s = s + idade
    if c == 1:
        hvelho = nome
        idadevelho = idade
    else:
        if sexo == 'M':
            if idade > idadevelho:
                idade = idadevelho
                hvelho = nome
    if sexo == 'F' and idade < 20:
        mulheres_novas += 1

media = s / 4
print(f'A média de idades é {media}')
print(f'O homem mais velho é {hvelho}')
print(f'{mulheres_novas} mulheres têm menos de 20 anos.')


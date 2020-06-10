'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
n = 0
tupla = ''
maior = 0
menor = ''
while n < 5:
    a = randint(0, 10)  # lembrar que o randint considera o último número
    if n == 0:
        maior = a
        menor = a
    else:
        if a > maior:
            maior = a
        elif a < menor:
            menor = a
    n += 1
    tupla += str(a) + ' '   # tupla = tupla + str(a) + ' '
print(f'Esses são os números sorteados: {tupla}')
print(f'O maior é {maior} e o menor, {menor}.')

# Jeito do professor:   ///////

n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))    # realmente é uma maneira bem inteligente
print(f'Eu sorteei os valores {n}')

# ou

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(n, end=' ')

print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')     # novos comandos

# Feito
# Ok
# Faça um programa que leia um número qualquer e mostre o seu fatorial (fazer com while e for).

n = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando {}!...'.format(n))
c = n
fat = 1     # Multiplicação 'limpa' começa em 1
while c > 0:
    print(f'{c}', end=' ')    # o espaço pode ficar dentro do texto, deixando o end vazio.
    print('x' if c > 1 else '=', end=' ')
    fat *= c    # ou fat = fat * c
    c -= 1

print('{}.'.format(fat))

# Agora com o for
num = int(input('Entre aqui um número inteiro: '))
fatorial = 1
for z in range(1, num + 1):
    fatorial = fatorial * z
    z = z + 1
print(f'{num}! = {fatorial}')

# Com módulo
from math import factorial
fato = factorial(num)
print(fato)

# ok. Me enrolei para fazer.

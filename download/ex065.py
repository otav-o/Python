# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lido. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

s = 0
q = 0
resp = 'S'
maior = 0
menor = 0
while resp == 'S': #or 'SIM':
    n = int(input('Digite um número: '))
    s = s + n
    if q == 0:
        maior = n
        menor = n
    elif q >= 1:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    q = q + 1
    resp = input('Quer continuar? ').upper().strip()

m = s / q
print('Você digitou {} números, e a média entre eles é {}. O maior número foi {} e o menor, {}.'.format(q, m, maior,
                                                                                                        menor))
# Feito

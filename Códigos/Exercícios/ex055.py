# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

x = []
for z in range(1, 6):
    peso = float(input('Insira o {}° peso: '.format(z)))
    x.append(peso)
x.sort()
print('O maior peso é {} e o menor, {}.'.format(x[4], x[0]))    # cuidado com o range da lista

# feito

# jeito do professor:
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é {} e o menor é {}.'.format(maior, menor))

# ok

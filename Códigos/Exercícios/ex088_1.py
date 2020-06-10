from random import randint
lista = list()
jogos = list()
print('-' * 30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
cont = cont2 = 0
while True:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            cont2 += 1
            break
    lista.sort()
    jogos.append(lista[:])  # uma cópia da lista
    lista.clear()
    if cont2 >= quant:
        break

print(f'Os números sorteados foram: {jogos}')
# Desisti. A solução dele é bem pior!
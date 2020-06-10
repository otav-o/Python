'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado  e as suas respectivas
posições na lista.'''

maior = menor = 0

numeros = list()

for c in range(0, 5):
    num = int(input('Digite um valor: '))   # numeros.append(int(input('Digite um valor'))
    if c == 0:
        maior = menor = num

    else:
        if num > maior:
            maior = num

        elif num < menor:
            menor = num

    numeros.append(num)
menores = numeros.count(menor)
p_menor = []


print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for pos, valor in enumerate(numeros):
    if valor == maior:
        print(pos, end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')

for pos, valor in enumerate(numeros):   # muito importante!
    if valor == menor:
        print(pos, end=' ')

# Ok

'''listanum.append(int(input(f'Digite um valor para a posição {0}')))
if c == 0: 
    mai = men = listanum[c]     # c é a última posição pois o número acabou de ser inserido'''


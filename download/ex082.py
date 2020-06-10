'''Dividindo valores em várias listas'''

numeros = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = ' '
    while resp not in ('SN'):
        resp = input('Quer continuar? ').strip().upper()[0]
    if resp == 'N':
        break

'''for i, v in enumerate(numeros):  # não entendi por que o professor usou o enumerate se o índice é irrelevante
    if v % 2 == 0:'''
print(f'Você digitou os números {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')

# feito
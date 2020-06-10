# Nome, peso, uma lista
temp = []   # not temp = dados = []
dados = []
maior = menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))

    if len(dados) == 0:
        maior = menor = temp[1]     # peso está na posição 1 de temp, e o nome na temp[0]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    dados.append(temp[:])   # dados recebe uma cópia da lista temporária
    temp.clear()
    perg = ' '
    while perg not in 'SN':
        perg = input('Quer continuar? ').strip().upper()
    if perg == 'N':
        break


print(f'Ao todo, você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi {maior:.1f}kg. Peso de ', end='')
for p in dados:     # p é a sublista de dados
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi {menor:.1f}kg. Peso de', end=' ')
for p in dados:
    if p[1] == menor:
        print(p[0], end=' ')

# Ok
# difícil



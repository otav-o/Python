print('Complete a matriz 3x3')
linha0 = [[], [], []]
linha1 = [[], [], []]
linha2 = [[], [], []]
for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]: '))
    linha0[c].append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [1, {c}]: '))
    linha1[c].append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [2, {c}]: '))
    linha2[c].append(n)

'''maiorlen = menorlen = 0
for i, v in linha2 + linha0 + linha1:
    if i == 0:
        maiorlen = len(v)
    else:
        if len(v) > maiorlen:
            meiorlen = len(v)

# print(f'{linha0:^{maiorlen}}')
'''

print(linha0)
print(linha1)
print(linha2)
# Consegui fazer, mas falhei no alinhamento das colunas




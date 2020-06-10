# Mais sobre matrizes
# soma dos valores pares, soma dos valores da terceira coluna, maior valor da segunda linha

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
terc_col = 0
maior = 0
for c in range(0, 3):
    for z in range(0, 3):
        n = int(input(f'Digite o valor da posição [{c}, {z}]: '))
        matriz[c][z] = n
        if n % 2 == 0:  # ou lá no final: if matriz[c][z] % 2 == 0
            par += n
        if matriz[c][2]:
            terc_col += n
        if matriz[1][z]:
            if z == 0:
                maior = n
            else:
                if n > maior:
                    maior = n

for c in range(0, 3):
    for z in range(0, 3):
        print(f'[{matriz[c][z]:^5}]', end='')
    print()
print(f'A soma dos números pares é {par}.')
print(f'A soma dos valores da terceira coluna é {terc_col}')
print(f'O maior valor da segunda linha é {maior}')

'''for n in matriz:    # imprime as sublistas
    print(n)'''

for l in range(0, 3):
    terc_col += matriz[l][1]
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(terc_col, maior)


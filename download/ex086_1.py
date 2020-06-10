matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for z in range(0, 3):
        matriz[c][z] = int(input(f'Digite o número para a posição [{c}, {z}]: '))
for c in range(0, 3):
    for z in range(0, 3):
        print(f'[{matriz[c][z]:^5}]', end=' ')    # imprimir os elementos
    print()

# OK
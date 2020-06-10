'''5 numeros input já com a lista ordenada sem usar o sort()'''

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        for pos in range(0, len(lista)):    # varrer a lista
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Inserido na posição {pos}.')
                break
        pos += 1
print(lista)
print('Fim do programa.')

# Ok
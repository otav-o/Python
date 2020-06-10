# Pares e ímpares em ordem crescente com apenas uma lista de input
# e com os números separados por sublistas
# 7 números
pares = []
impares = []
numeros = [pares, impares]
for c in range(0, 7):
    n = int(input(f'Digite um valor![{c + 1}/7] '))
    pares.append(n) if n % 2 == 0 else impares.append(n)
pares.sort()
impares.sort()
print(f'Os pares digitados foram: {pares} e os ímpares, {impares}')

# Feito.
# Resposta oficial:

núm = [[], []]
for c in range(1, 8):
    valor = int(input('Um número: '))
    if valor % 2 == 0:
        núm[0].insert(1, valor)
    else:
        núm[1].append(valor)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}'
      f'\nOs valores ímpares foram: {núm[1]}')

# Feito. Ok

'''numeros em lista sem repetição, ordem crescente'''

lista = []
while True:
    n = int(input('Digite um valor: '))
    if lista.count(n) == 0:     # ou if n not in lista
        lista.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Esse valor já está na lista.')
    perg = ' '
    while perg not in 'SN':
        perg = input('Quer continuar? ').strip().upper()[0]
    if perg == 'N':
        break
print('-=' * 20)
# ou lista.sort()
print(f'Você digitou os valores {sorted(lista)}')

# Feito. Ok

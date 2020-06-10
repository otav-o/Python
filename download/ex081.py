'Extrair dados de uma lista'

lista = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    perg = ' '
    while perg not in 'SN':
        perg = input('Deseja continuar? ').upper().strip()[0]
    if perg == 'N':     # a identação define qual while será quebrado
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)    # parece que não é possível colocar esse comando dentro do print
print(f'Os valores em ordem decrescente são: {lista}')
print(f'O número 5 faz parte da lista' if lista.count(5) != 0 else 'O número 5 não faz parte da lista.')

# ou if 5 in lista...

# Feito. Ok

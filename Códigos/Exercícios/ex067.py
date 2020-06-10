# Faça um programa que mostre a tabuada de vários números, um de cada valor digitado pelo usuário. O programa será
# interrompido quando o número solicitado for negativo.
print('-=' * 20)
print('{:^40}'.format('Gerador de tabuada!'))
print('-=' * 20)
q = s = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    s += n
    q += 1
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    resp = input('Deseja continuar? ').upper().strip()
    if resp[0] == 'N':
        break
print('Fim do programa! Você solicitou {} tabuadas. E a soma dos números que você digitou é {}'.format(q, s))

# Feito.
# ok

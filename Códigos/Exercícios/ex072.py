''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20
Seu programa deverá ler um número pelo teclado (entre zero e 20) e mostrá-lo por extenso.'''

a = ('zero', 'um', 'dois', 'três', 'quatro',
     'cinco', 'seis', 'sete', 'oito', 'nove',
     'dez', 'onze', 'doze', 'treze', 'catorze',
     'quinze', 'dezesseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')
resp = ' '
while True:
    b = int(input('Digite um número de 0 a 20: '))

    while b < 0 or b > 20:
        b = int(input('Tente novamente. Entre 0 e 20: '))

    print(f'Você digitou o número {a[b]}.')
    resp = ' '  # precisei voltar com o valor de resp
    while resp not in 'SN':
        resp = str(input('Você quer continuar? ')).upper().strip()[0]
    if resp == 'N':
        break


# Resolução do professor:
while True:
    num = int(input('Digite &8 um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')

# Feito.
# Ok    'não é a melhor maneira de se escrever por extenso'
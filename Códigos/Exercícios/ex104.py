def leiaInt(num):
    while classmethod(num) == 'str':
        print('\033[034nERR0! Digite um número inteiro válido.')
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
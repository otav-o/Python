def fatorial(n, resp=0):
    """
    Calcula o fatorial de um número
    :param n: número base do cálculo
    :param resp: True: mostra a conta (opcional)
    :return: O fatorial de n
    """
    fat = 1
    for c in range(n, 0, -1):
        fat *= c
    if resp == True:
        for c in range(n, 0, -1):
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = {fat}')

    else:
        print(fat)


fatorial(10)
fatorial(5)
fatorial(10, True)
fatorial(6, False)
fatorial(7, True)
fatorial(4, True)

# Feito

# Resposta do professor:
def fat(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fat(5, show=True))
print(fat(5))
print(fat(5), True)
print(fat(5, True))
fat(5)

# Feito, ok

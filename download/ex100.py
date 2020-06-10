# Duas funções: uma para sortear valores e outra para somar os números pares
from random import randint


def sortear(n):
    """Insira quantos valores você quer sortear
    de um a dez"""

    lista = []
    for c in range(0, n):
        lista.append(randint(1, 10))
    print(f'Sorteando {n} valores: {lista}')
    return(lista)


def somar_pares(lst):
    """Soma os valores pares de uma lista"""

    s = 0
    for v in lst:
        if v % 2 == 0:
            s += v
    print(f'A soma dos valores pares de {lst} é {s}.')


somar_pares(sortear(5))

# Feito. Ok
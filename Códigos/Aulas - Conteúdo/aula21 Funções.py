''' Interactive Help;'''

# help() no console interativo, ou

# help(print)     #, ou

# print(print.__doc__)    # informações que podem ser diferentes


'''Docstrings'''  # 'manual'


def contador(i, f, p):
    '''
    Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Criada por Otávio
    '''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(0, 100, 10)
help(contador)

'''Argumentos/ parâmetros opcionais'''


def somar(a, b, c=0):  # se c nada receber, ele vale zero. C é parâmetro opcional
    s = a + b + c
    print(f'A soma vale {s}.')


# nada impede todos os parâmetros serem opcionais. Digitar somar(), neste caso, deixaria s == 0

somar(3, 2, 5)
somar(8, 4)
somar(b=4, a=2)

'''Escopo de variáveis'''


def teste():
    x = 8  # escopo local (só está na def)
    print(f'Na função teste, n vale {n}')  # roda com n = 2, mesmo este criado antes da função ser chamada.
    print(f'Na função teste, x vale {x}')


n = 2  # escopo global (serve para todo o programa)
print(f'No programa principal, n vale {n}')
teste()


# print(f'No programa principal, x vale {x}')     # x não está definido

def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
função()
print(f'N1 fora vale {n1}')


def testando(b):
    global a
    a = 8  # sem o comando global, a de fora != a de dentro
    b += 4
    c = 2
    print(f'Dentro: A = {a}, B = {b} e C = {c}')


a = 5
testando(a)
print(f'Fora: A = {a}')

'''Retorno de resultados.'''


def multiplicar(a=0, b=1, c=1):
    mult = a * b * c
    # print(f'O produto dá {mult}')
    return mult


r1 = multiplicar(5, 3)
r2 = multiplicar(4, 2, 3)
r3 = multiplicar(2)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')

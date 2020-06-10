def lin():
    print('-' * 30)


def mensagem(msg):
    print('-' * 30)
    print(f'{msg.upper():^30}')     # msg é um parâmetro
    print('-' * 30)


def soma(a, b):
    s = a + b
    print(s)


def soma1(*num):    # desempacotamento
    s = 0
    for v in num:
        s += v
    print(f'A soma de {num} é {s}')


def contador(*num):
    print(f'Recebi os valores {num} que são {len(num)} números!')   # num tupla


def dobra(lst):     # receber uma lista e dobrar seus valores. Também funciona se desempacotar.
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lin()
print(f"{'GERADOR DE NÚMEROS':^30}")
lin()
print(f'{"LOTERIA":^30}')
lin()


mensagem('sistema de alunos')   # parâmetro: sistema de alunos


soma(4, 5)
soma(a=4, b=5)      # explicitar é opcional; se for feito, deve ser para todos os parâmetros
soma(8, 9)
soma(b=8, a=9)
soma(2, 1)


contador(4, 5, 3, 2, 15)
contador(1, 2, 5)


valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)


soma1(5, 6, 2, 3, 4, 1, 2)

help(soma1)
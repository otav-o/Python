# Função de contador
from time import sleep


def contador(a, b, c=1):
    print('\n-=', end='')
    print('-=' * 19)
    print(f'Contagem de {a} até {b} de {c} em {c}:')
    if b < a and c > 0:
        c = -c
    if b > 0:
        b += 1
    elif b <= 0:
        b -= 1
    for d in range(a, b, c):
        print(d, end=' ')
        sleep(0.5)


contador(1, 10)
contador(10, 0, 2)
print('\nAgora é a sua vez de personalizar a contagem!')
i = int(input(f"{'Início: ':<8}"))
f = int(input(f"{'Fim: ':<8}"))
p = int(input(f"{'Passo: ':<8}"))
contador(i, f, p)

# Feito. Completamente diferente da resposta oficial


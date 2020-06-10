# Função maior, que receba vários parâmetros e diga qual é o maior número.
def maior(*x):
    maior = 0
    for c in range(0, len(x)):
        if c == 0:
            maior = x[c]
        else:
            if x[c] > maior:
                maior = x[c]
        # c += 1
    print('=-' * 20)
    print(f'''Analisando os valores passados...
{x} -> Foram informados {len(x)} valores ao todo.
O maior valor é {maior}''')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# Feito. Ok
# Validador de expressão numérica; contagem de parênteses

ex = input('Digite uma expressão matemática! ')
if ex.count('(') == ex.count(')'):
    print('Essa expressão é válida')
else:
    print('Essa expressão é inválida.')

# Jeito do professor:   (estranho pois me parece a pior maneira)

pilha = []
for simb in ex:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:  # significa que já foi colocado um '(' lá
            pilha.pop()
        else:   # se pilha está vazio é porque já removeu todos os parênteses ou o primeiro é ')'
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Válida')
else:
    print('inválida')

# Feito. Ok
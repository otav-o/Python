# Refaça o ex035 acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero (3 lados iguais), isósceles (2 lados iguais), Escaleno (todos diferentes)

l1 = float(input('Insira um dos lados do triângulo: '))
l2 = float(input('Insira o segundo lado: '))
l3 = float(input('O último: '))

if l1 == l2 == l3:
    tipo = 'EQUILÁTERO'
elif l1 == l2 or l2 == l3 or l1 == l3:
    tipo = 'ISÓSCELES'
else:
    tipo = 'ESCALENO'

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os três segmentos formam um triângulo \033[31m{}\033[m'.format(tipo))
else:
    print('Não formam um triângulo.')

# Gostei.
# O professor colocou um if dentro de outro

# Outra maneira;
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses segmentos podem formar um triângulo.', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:  # observar que a desigualdade deve ser redundante
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não podem formar um triângulo')
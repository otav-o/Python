# Desenvolva um programa que leia o comprimento das três retas e diga ao usuário se elas podem ou não formar um
# triângulo
l1 = int(input('Insira um dos lados: '))
l2 = int(input('Insira o segundo: '))
l3 = int(input('O último: '))

if l1 + l2 <= l3:
    print('Não forma um triângulo.')
elif l2 + l3 <= l1:
    print('Não forma um triângulo.')
elif l1 + l3 <= l2:
    print('Não forma um triângulo.')
else:
    print('Forma um triângulo.')


if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Esses segmentos podem formar um triângulo.')
else:
    print('Esses segmentos não podem formar um triângulo.')
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a seguinte mensagem:
# O primeiro valor é o maior
# O segundo valor é o maior
# Os dois valores são iguais

print('\033[34mComparador de números!\033[m')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Não é possível comparar. Os dois valores são iguais.')

# feito. ok

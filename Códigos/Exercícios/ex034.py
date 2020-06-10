# Escreva um programa que calcule o aumento do salário de um funcionário
# aumento de 10% para salários acima de 1250
# inferiores ou iguais: 15%

s = float(input('Insira o valor do seu salário: '))
if s <= 1250:
    s2 = 1.15 * s
else:
    s2 = 1.10 * s
print('Seu salário reajustado é de', s2)
# {:.2f}
'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: considere que o caixxa possui cédulas de R$50, R$20, R$10 e R$1'''

print('-=' * 20)
print('{:^40}'.format('Caixa eletrônico'))
print('-=' * 20)

valor = int(input('Qual o valor do saque? R$'))
c50 = valor // 50
resto = valor % 50
c20 = resto // 20
resto = resto % 20
c10 = resto // 10
resto %= 10
c1 = resto

if c50 != 0: print(f'{c50} cédulas de R$50,00')
if c20 != 0: print(f'{c20} cédulas de R$20,00')
if c10 != 0: print(f'{c10} cédulas de R$10,00')
if c1 != 0: print(f'{c1} cédulas de R$1,00')    # que horrível

'''Feito. Funciona. Mas olhe a resposta que usa os conceitos da aula'''

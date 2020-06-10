# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador, e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela
# não pode exceder 30% do salário, ou então o empréstimo será negado.

print('''\033[34m________________________\033[m
\033[32mBem vindo ao simulador habitacional. Preencha os dados abaixo para solicitar o financiamento.\033[m
\033[34m_________________________\033[m''')

nome = input('Qual é o seu nome? ')
sal = int(input('{}, qual o seu salário mensal? '.format(nome)))
valor = int(input('Qual o valor da casa? '))
anos = int(input('Em quantos anos você pretende pagar? '))

from time import sleep
print('\033[31mXXXXXX CALCULANDO XXXXXX\033[m')
sleep(3)

if valor / (12 * anos) > 30/100 * sal:
    print('Desculpa, {}!. Seu empréstimo foi negado.'.format(nome))
else:
    print('Empréstimo aprovado!! O valor da prestação mensal será de: R${:.2f}'.format(valor / (12 * anos)))

# feito; ok
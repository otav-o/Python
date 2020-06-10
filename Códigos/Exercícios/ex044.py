# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# - à vista dinheiro/ cheque: 10% de desconto;
# - à vista no cartão: 5% de desconto;
# - em até 2x no cartão: preço normal;
# - 3x ou mais no cartão: 20% de juros.

print('{:=^40}'.format('LOJAS GUANABARA'))

preço = float(input('Calculadora de caixa! Insira o preço do produto: '))

print('''FORMAS DE PAGAMENTO:
1 - à vista dinheiro/ cheque: 10% de desconto;
2 - à vista no cartão: 5% de desconto;
3 - em até 2x no cartão: preço normal;
4 - 3x ou mais no cartão: 20% de juros.''')

forma = int(input('Digite o número referente à forma de pagamento. '))
if forma == 1:
    total = 0.9 * preço
elif forma == 2:
    total = 0.95 * preço
elif forma == 3:
    total = preço
elif forma == 4:
    total = 1.2 * preço
else:
    total = preço
    print('Opção inválida de pagamento.')
print(f'O valor final a ser pago é R${total:.2f}, pois foi escolhida a opção {forma}.')

# Estava dando erro pois 'forma' estava como string. Então o programa pulava as condições, dizendo que 'total'
# não estava definido
# ficou menor do que o do professor

# E esse novo print formatado recomendado pelo pycharm?

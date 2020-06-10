# Desenvolva um programa que peça a distância de uma viagem em quilômetros. Calcule o preço da viagem, cobrando
# R$0,50/km para viagens de até 200km e R$0,45 para viagens mais longas.
d = float(input('Qual a distância em km da viagem? '))

c = d * 0.5 if d <= 200 else d * 0.45
# if d > 200:
#    c = d * 0.45
# else:
#    c = d * 0.5
print('O custo total é R${:.2f}'.format(c))

# obs.: linha 5 - não é 'c = d * 0.5 if d <= 200 else c = d * 0.45'
# ok

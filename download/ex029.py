# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
# 7 reais por cada km/h acima do limite

v = float(input('Calculadora de multas. Digite sua velocidade: '))
if v > 80:
    m = (v - 80) * 7
    print('Você foi multado em {:.2f} reais por passar {:.2f} km/h acima do limite'.format(m, v - 80))
else:
    print('Parabéns! Você não foi multado.')

# Feito. ok
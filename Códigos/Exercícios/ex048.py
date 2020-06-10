# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
soma = 0
quantidade = 0
for c in range(1, 501, 2):
    if c % 2 != 0 and c % 3 == 0:
        soma = soma + c
        quantidade = quantidade + 1  # importante

print('A soma dos {} números ímpares múltiplos de 3 localizados entre 1 e 500 é: {}'.format(quantidade, soma))

# feito. Resultado: 20667 [correto]
# ok
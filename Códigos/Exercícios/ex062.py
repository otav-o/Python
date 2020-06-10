# Melhore o desafio 61, perguntando se o usuário quer mostrar mais alguns termos. O programa encerra quando ele disser
# que quer mostrar 0 termos.

print('x=' * 20)
print('{:^40}'.format('Calculadora de PA - de novo'))
print('x=' * 20)

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão? '))
c = 1   # O primeiro termo de uma PA deve ser representado pelo algarismo 1
print('Os 10 primeiros termos dessa PA são:')
while c < 11:
    print('{}'.format(a1 + (c - 1) * r), end='')
    print(', ' if c < 10 else '.', end='')
    c = c + 1
'''perg = input('\nVocê deseja mais termos? [Sim/ Não] ').upper().strip()
if perg == 'SIM' or 'S':
    n = int(input('Quantos? '))
elif perg == 'NÃO' or 'N' or 'NAO':
    print('Ok! Fim do programa')
else:
    print('Resposta inválida! Reinicie o programa.')    # Não sei fazer repetição aqui :(
   '''
resp = 1
an = a1 + 10 * r

while resp != 0:
    resp = int(input('\nDigite mais quantos termos você deseja: '))
    print('{}'.format(an + (resp + 10 - 1) * r), end='')




# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = input('Qual é o seu nome completo? ').strip()
if 'SILVA' in nome.upper():
    print('Você tem Silva no nome!')
else:
    print('Você não é da família Silva.')

# Feito. Funciona mesmo que 'silva' esteja dentro de uma outra palavra.


# Faça um programa que leia o nome completo de uma pessoa e, em seguida, mostre o primeiro e último nomes, separadamente

nome = input('Qual é o seu nome completo? ').strip()
n1 = nome.split()[0]    # importante saber isso
n2 = nome.split()[len(nome.split()) - 1]
print('''O primeiro nome é {}.
O último, {}.'''.format(n1, n2))

# Feito.

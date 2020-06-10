# Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maíusculas
# b) O nome com todas as minúsculas
# c) Quantas letras ao çtodo (sem considerar espaços)
# d) Quantas letras tem o primeiro nome
# 16/03/2020, coronavirus cancelou minhas aulas amanhã

nome = input('Qual é o seu nome completo? ').strip()
a = nome.upper()
b = nome.lower()
# c = len(''.nome.join())
# d = nome.split()
# e = len(d[0])

# c = len(nome.remove(' '))   # não existe 'remove' para string
c = len(nome) - nome.count(' ')  # ótimo
d = len(nome.split()[0])  # existe 'len' de lista

print('O seu nome em caracteres maúsculos é {}, em minúsculos, {}. Possui {} letras e o primeiro nome tem {}.'
      .format(a, b, c, d))

# Feito.

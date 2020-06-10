# Crie um programa que leia 3 números e fale qual é o maior e qual é o menor.
n1 = int(input('Escreva um número: '))
n2 = int(input('Outro: '))
n3 = int(input('O terceiro: '))

num = []
num.append(n1)
num.append(n2)
num.append(n3)
num.sort(reverse=True)

a = num[0]
c = num[2]

print('O maior número é {} e o menor é {}'.format(a, c))

# Não fiz pela estrutura condicional. E usei muitas linhas.

# Resolução do professor:
menor = n1  # e não n1 = menor (a ordem importa)
if n2 < n3 and n2 < n1:
    menor = n2  # A ORDEM IMPORTA (tava n2 = menor)
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1  # e não n1 = maior (a ordem importa)
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior número: {}'.format(maior))
print('O menor número: {}'.format(menor))

# DEU CERTO. ATENÇÃO À ORDEM DE QUEM RECEBE OS VALORES.


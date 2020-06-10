from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Outro aluno: ')
a3 = input('O terceiro: ')
a4 = input('O último: ')

lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem sorteada é: {}'.format(lista))


#feito
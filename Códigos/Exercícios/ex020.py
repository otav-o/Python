# Sortear a ordem de apresentação dos alunos
from random import choice
print('Diga o nome dos estudantes para o sorteio da ordem de apresentação dos trabalhos.')
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('O terceiro: ')
a4 = input('O último: ')
lista = [a1, a2, a3, a4]

s1 = choice(lista)
lista.remove(s1)
s2 = choice(lista)
lista.remove(s2)
s3 = choice(lista)
lista.remove(s3)
s4 = choice(lista)

print('A ordem de apresentação é: {}, {}, {}, {}'.format(s1, s2, s3, s4))

#feito
 
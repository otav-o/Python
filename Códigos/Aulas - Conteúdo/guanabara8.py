# 16. Crie um programa que leia um número real e retorne a sua parte inteira

num1 = float(input('Digite um número: '))
from math import floor, trunc
print('A parte inteira de {} é {}!'.format(num1, floor(num1)))
print(trunc(num1))
print(int(num1))    #OK

# 17. Triângulo retângulo

cateto1 = float(input('Insira a medida de um dos catetos: '))
cateto2 = float(input('Quanto mede o outro cateto? '))

from math import sqrt

hipotenusa = sqrt(cateto1 ** 2 + cateto2 ** 2)
# x = [cateto1, cateto2, hipotenusa]
# if cateto2 == cateto1 + 1:
# elif hipotenusa == cateto2 + 1:
# print('Esse triângulo é pitagórico e suas dimensões são: {}, {} e {}!'.format(cateto1, cateto2, hipotenusa))
# else:
# print('A hipotenusa mede {}!') VOLTAR AQUI UM DIA E TENTAR

print('A hipotenusa mede {}!'.format(hipotenusa))
# math.hypot(co, ca)





# 20 sortear também a ordem dos alunos

print('Agora vou fornecer a ordem de apresentação dos trabalhos desses mesmos alunos.')

# alunos = []

# import emoji

# print(emoji.emojize(':sunglasses:', use_aliases=True))

# 21 tocar uma música mp3

# em outro programa


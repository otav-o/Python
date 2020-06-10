#Aula 8 - módulos
#Importar biblioteca 'math'

#ceil: arredondamento para cima 
#floor: para baixo
#trunc: truncar, elimina oq tem depois da vírgula sem nenhum arredondamento
#pow: potÊncia, **
#sqrt: raiz quadrada
#factorial
#
#import math: importa tudo
#    ou
#from math import sqrt
#from math import sqrt, ceil




import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)   #precisa citar o math antes

## raiz = sqrt(num) # erro: sqrt não está definido

print('A raiz de {} é igual a {:.2f}.'.format(num, raiz))
print('A raiz de {} arredondada para cima é igual a {}.'.format(num, math.ceil(raiz)))

print('A raiz de {} arredondada para baixo é igual a {}.'.format(num, math.floor(raiz)))


#OK


# Biblioteca random

import random
num = random.random()
print(num)

num2 = random.randint(9, 89)
print (num2)





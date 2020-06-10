# 04/05/2020
# Tuplas - váriável composta. Armazenam vários valores
# As tuplas são imutáveis!

# () ou nada -> tuplas
# [] -> listas
# {} -> dicionários


lanche = 'hambúrguer'
lanche = 'suco'
print(lanche)   # suco

lanche = 'Hambúrguer', 'suco', 'pizza', 'pudim'
print(lanche)   # ('Hambúrguer', 'suco', 'pizza', 'pudim')
print(lanche[1])    # suco
print(lanche[-2])   # pizza
print(lanche[1:3])  # 1, 2 ('suco', 'pizza')
print(lanche[2:])   # pizza -> fim ('pizza', 'pudim')
print(lanche[:2])   # ('Hambúrguer', 'suco') desconsiderando o último
print(lanche[-2:])  # ('pizza', 'pudim') os dois pontos depois do índice indicam que ele é o início. 'Do menos 2 até o
                                                                                                              # final'
# lanche[1] = 'oi'    # Não é possível atribuir um valor a uma posição da tupla depois de ela já ter sido criada.
lanche = 'oi'       # Isso é possível
print(lanche)

lanche = ('bala', 'salgado', 'bolo', 'milho', 'batata')

# Três maneiras de usar a estrutura for com tuplas: ////////////q

for comida in lanche:   # para cada comida em lanche
    print(f'Vou comer {comida}')

for cont in range(0, len(lanche)):  # com o contador é possível mostrar as posições
    print(f'Vou comer {lanche[cont]}, posição {cont}')     # o cont está valendo 1, 2, 3, 4.

for pos, comida in enumerate(lanche):   # for var1, var2 in enumerate(tupla)
    print(f'Eu vou comer {comida}. Posição {pos}')  # também mostra a posição

print(len(range(1, 5)))     # 4
print(len(range(0, 5)))     # 5
# lembrar de começar do zero no caso das tuplas. -> mostra todos os elementos

# Observação: o último termo do range não é contado, mas isso não impede de mostrar o último termo da tupla.
# Lembre-se de que os índices começam em zero, logo o range(0, 5) do exemplo atende os índices 0, 1, 2, 3 e 4
# que formam a tupla de len = 5. Ou seja: range(0, len(tupla)).

print(sorted(lanche))   # ['bala', 'batata', 'bolo', 'milho', 'salgado']
# classifica em ordem alfabética mas não altera a tupla, observe os colchetes de lista


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a   # != a + b
print(c)    # (5, 8, 1, 2, 2, 5, 4)

print(c.count(5))   # 2 - quantas vezes aparece o elemento 5
print(c.index(2))   # 3 - posição da *primeira ocorrência* do elemento 3 // tupla.index()
print(c.index(5))   # 0
print(c.index(5, 1))    # 5 - posição da primeira ocorrência a partir da posição 1 // tupla.index(elemento, começo)
# 'deslocamento'

del lanche
print(lanche)   # não está definido

# fazer uma apostila de Python
# Fatiamento de tuplas
# Faça um exercício que leia uma frase no teclado e determine:
# a) Quantas letras 'a' aparecem.
# b) Em que posição essa letra aparece pela primeira vez.
# c) Em que posição ela aparece pela última vez.

# frase = input('Digite uma frase: ').strip()
# v = frase.upper().count('A')

# print('A letra "a" aparece {} vezes. A primeira vez foi na posição {} e a última na posição {}.'
#      .format(v, frase.upper().find('A') + 1, frase.upper().find('A')[len() - 1]))

# descobri que 'ã' é diferente de 'a'


# Tentando de novo

f = input('Digite uma frase: ').strip()
v = f.lower().count('a')
p = f.lower().find('a') + 1
u = f.lower().rfind('a') + 1  # ***

print('A letra "a" aparece {} vezes. A primeira vez foi na posição {} e a última na posição {}.'
      .format(v, p, u))

# Ok

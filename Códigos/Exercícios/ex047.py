# Crie um programa que mostre na tela todos os números pares que estão no inervalo entre 1 e 50.

for c in range(0, 51, 2):   # colocar de 2 em 2 faz o processador trabalhar menos - metade das iterações / laços.
    if c % 2 == 0:  # o resto da divisão de um número par por 2 é sempre zero.
        print(c, end=', ')

# print('Todos os números pares do intervalo 1-50 são: \033[31m{}\033[m.'.format(n))

# deu certo
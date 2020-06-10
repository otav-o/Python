#Sintaxe diferente

nome = input('Qual é o seu nome? ')
print('O seu nome é {}'.format(nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))


algo = input('Digite algo: ')

if algo.isnumeric() == True:
    print('{} é um número!'.format(algo))

print('{} é da {}'.format(algo, type(algo)))


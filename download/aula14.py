# A estrutura 'for' tem um limite (range); a repetição while roda enquanto o teste lógico não der False. Usado quando a
# distância até o fim é desconhecida, roda indefinidamente. Ressaltando: é uma estrutura de repetição com teste lógico.

'''for c in range(1, 10):
    print(c)
print('fim')

d = 1
while d < 10:
    print(d)
    d += 1
print('fim')'''

n = 1
p = 0   # p = i = 0
i = 0
while n != 0:
    n = int(input('Digite um valor! '))
    if n % 2 == 0:   # par
        p += 1
    else:
        i = i + 1
print('Fim. Foram digitados {} números pares e {} ímpares.'.format(p, i))

# o zero entra na análise de par/ ímpar, pois o n só recebe zero depois da estrutura while já ter começado. Observe que,
# antes do input, n ainda é diferente de zero. Para remover o zero e deixá-lo apenas como um meio de terminar o
# programa, deve-se colocar um if ali:

'''while n != 0:
    n = int(input('Digite um valor! '))
    if n != 0:
        if n % 2 == 0:   # par
            p += 1
        else:
            i = i + 1'''


g = 's'     # senão a repetição não começa
while g == 's':
    valor = int(input('Digite um valor: '))
    g = input('Quer continuar? [S/N] ').lower()
print('FIM')    # só sai da estrutura while quando o teste lógico dá False.

while True:     # Roda infinitamente
    resp = input('Deseja continuar? ').lower()
    if resp == 'n':
        break   # Interrompe a estrutura while
print('Fim')

n = s = 0
while n != 999:
    s += n
    n = int(input('Digite um número: '))

# s -= 999    # gambiarra para remover o flag. Em um exercício anterior eu usei um if para evitar a soma.

# Pera. Consigo remover o 999 apenas colocando a soma antes do input. Nesse caso, como o 999 seria a última linha do
# loop, iria finalizá-lo sem qualquer soma.

print('A soma vale {}'.format(s))

# usando o break:   /////////////////////////////

n = s = cont = 0   # "inicializador"
while True:
    n = int(input('Insira um número. '))
    if n == 999:
        break   # O laço acaba aqui
    s = s + n
    cont = cont + 1
print('A soma desses {} números vale {}.'.format(cont, s))


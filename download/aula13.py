# Iterações, Laços de repetições
# for: estrutura de repetição com variável de controle.

print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('---')

for c in range(1, 6):   # apenas 5 vezes; se quiser 6, ponha (0, 6)
    print('Olá')
print('FIM')
print('---')

for c in range(0, 6):
    print('Sim')
    print('Não')
print('---')

for h in range(0, 7):   # 0, 1, 2, 3, 4, 5, 6 (7 itens)
    print(h)
print('---')

for t in range(6, 0, -1):  # 6, 5, 4, 3, 2, 1 (6 itens)
    print(t)
print('---')

for y in range(0, 7, 2):   # 0, 2, 4, 6
    print(y)
print('---')

n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('---')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for w in range(i, f + 1, p):
    print(w)
print('---')


s = 0
for p in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n  # s = s + n
print('O somatório de todos os valores foi {}'.format(s))

# Nesse último caso: p faz parte da estrutura de iteração, é o 0, 1, 2 e 3
#                    n é cada um dos valores digitados. A cada repetição, soma-se ao s, modificando o valor dele.

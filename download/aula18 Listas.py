# Listas compostas

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = '22'
galera.append(teste[:])
print(galera)

galera.clear()
#

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas[1])
print(pessoas[0][1])
print()
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos.')

#
print()
galera = list()
dado = list()   # lista temporária
for c in range(0, 3):   # ler e jogar uma cópia dentro da lista principal
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print()
for p in galera:
    if p[1] > 21:
        print(f'{p[0]} tem mais de 21 anos.')

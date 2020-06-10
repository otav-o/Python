filme = {'nome': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

print(filme['nome'])
# print(filme[0])     # erro


for k, v in filme.items():  # items() substitui o enumerate
    print(f'O {k} é {v}')

#
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
pessoas['nome'] = 'Leandro'  # se 'nome' não existir, ele será criado
del pessoas['sexo']
pessoas['peso'] = 98.5  # é a mesma coisa do comando append
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)

print()
#

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # brasil.append(estado[:])     não funciona
    brasil.append(estado.copy())
print(brasil)  # Observe os três dicionários dentro da lista, e como 'estado' variou no range

for e in brasil:  # para cada estado em brasil
    for k, v in e.items():  # chave e valor em itens do estado
        print(f'{k} = {v}')
for e in brasil:
    for v in e.values():
        print(v)

from operator import itemgetter
'''lista = sorted(dicionario.items(), key=1, reverse=True)'''

# Unindo dicionários e listas; fazer uma lista de dicionários
lista = list()
pessoa = dict()
while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: ').strip().upper()[0]
        if pessoa['sexo'] in 'MF':      # validação de dados
            break
        print('Erro. Digite somente M ou F')

    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())       # "pessoa" é um dicionário auxiliar que zera a cada loop
    perg = ' '
    while perg not in 'sn':
        perg = input('Quer continuar? ').strip().lower()[0]
    if perg == 'n':
        break

soma = 0
mulheres = list()
maiores = list()

for c in range(0, len(lista)):
    soma += lista[c]['idade']
    if lista[c]['sexo'] == 'F':
        mulheres.append(lista[c]['nome'])
media = soma / len(lista)       # seria mais fácil obter a soma no input() e calcular a média no print()
                                # soma += pessoa['idade']
for c in range(0, len(lista)):
    if lista[c]['idade'] > media:
        maiores.append(lista[c]['nome'])


print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram: {mulheres}')
print(f'D) Lista de pessoas que estão com idade acima da média: {maiores}')

# Feito. Ok (um pouco diferente)
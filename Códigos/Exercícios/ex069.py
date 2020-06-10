# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# a) quantas pessoas têm mais de 18 anos;
# b) quantos homens foram cadastrados;
# c) quantas mulheres têm menos de 20 anos.
# perguntar novamente se a resposta for inválida

maiores = 0
homens = 0
mul20 = 0   # fazer tudo isso em uma só linha
num = 0
sexo = ' '  # não pode ficar vazio
while True:
    print('-' * 20)

    nome = input('Digite o nome: ')
    idade = int(input('Idade: '))
    if idade > 18:
        maiores += 1
    while sexo not in 'MF':
        sexo = input('Sexo: ').upper().strip()[0]   # não funcionou colocar o [0] no sexo da linha de baixo
    print('-' * 20)
    if sexo == 'F' and idade < 20:
        mul20 += 1
    if sexo == 'M':
        homens += 1
    num += 1
    perg = 'bom dia bolsonaro'
    while perg not in 'SN':
        perg = input('Continuar? ').upper().strip()
    if perg[0] == 'N':                              # mas funcionou aqui (?)
        break

print('''Foram cadastradas {} pessoas.
{} têm mais de 18 anos.
Há {} homens.
{} mulheres têm menos de 20 anos.'''.format(num, maiores, homens, mul20))


# Funciona, mas está incompleto.
# Consertei. Ok

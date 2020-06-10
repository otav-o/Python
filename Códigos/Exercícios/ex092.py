# Cadastro de trabalhador em Python
from datetime import date
dados = dict()
while True:
    dados['nome'] = input('Nome: ')
    nasc = int(input('Ano de nascimento: '))
    idade = nasc - date.today().year
    dados['idade'] = idade
    dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if dados['ctps'] == 0:
        break
    contrat = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: '))
    dados['aposentadoria'] = contrat + 65
    break

print('=-' * 20)
for k, v in dados.items():
    print(F'{k} tem o valor {v}')
# feito ok